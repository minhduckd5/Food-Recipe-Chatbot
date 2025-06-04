from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from antlr4 import *
from CompiledFile.ChatLexer import ChatLexer
from CompiledFile.ChatParser import ChatParser
from CompiledFile.ChatListener import ChatListener
import os
import ollama

app = Flask(__name__, 
            static_folder='templates',
            template_folder='templates')
CORS(app)

# Initialize Ollama with a recipe-focused model
# You can use different models like 'llama2', 'mistral', etc.
OLLAMA_MODEL = "gemma3:12b-it-qat"

class RecipeChatListener(ChatListener):
    def __init__(self):
        self.response = ""
        self.user_input = ""
        self.show_reasoning = False
        
    def enterSearch_recipe(self, ctx):
        recipe_name = ctx.recipe_name().getText()
        self.user_input = f"Find a recipe for {recipe_name}. Include a brief description, ingredients, and instructions."
        self._get_ollama_response(self.user_input)
        
    def enterGet_ingredients(self, ctx):
        recipe_name = ctx.recipe_name().getText()
        self.user_input = f"List all the ingredients needed for {recipe_name}."
        self._get_ollama_response(self.user_input)
        
    def enterGet_instructions(self, ctx):
        recipe_name = ctx.recipe_name().getText()
        self.user_input = f"Give me step-by-step instructions to make {recipe_name}."
        self._get_ollama_response(self.user_input)
        
    def enterSuggest_recipe(self, ctx):
        if ctx.ingredient_name():
            ingredient = ctx.ingredient_name().getText()
            self.user_input = f"Suggest a recipe that uses {ingredient}."
        else:
            self.user_input = "Suggest a popular recipe."
        self._get_ollama_response(self.user_input)
        
    def enterDietary_restriction(self, ctx):
        diet = ctx.DIET().getText()
        self.user_input = f"Suggest a {diet} recipe. Include a description, ingredients, and instructions."
        self._get_ollama_response(self.user_input)
        
    def enterCooking_time(self, ctx):
        recipe_name = ctx.recipe_name().getText()
        self.user_input = f"How long does it take to cook {recipe_name}?"
        self._get_ollama_response(self.user_input)
        
    def enterSubstitution(self, ctx):
        ingredient = ctx.ingredient_name().getText()
        self.user_input = f"What can I use as a substitute for {ingredient} in a recipe?"
        self._get_ollama_response(self.user_input)
        
    def enterCooking_tip(self, ctx):
        if ctx.recipe_name():
            name = ctx.recipe_name().getText()
            self.user_input = f"Give me a useful cooking tip for {name}."
        elif ctx.ingredient_name():
            name = ctx.ingredient_name().getText()
            self.user_input = f"Give me a useful cooking tip about {name}."
        else:
            self.user_input = "Give me a general cooking tip."
        self._get_ollama_response(self.user_input)
        
    def enterHelp(self, ctx):
        self.response = (
            "Available commands:\n"
            "- search/find/show recipe for [recipe name]\n"
            "- show/list/what are ingredients for/of [recipe name]\n"
            "- show/how to make/how do I make/instructions for [recipe name]\n"
            "- suggest/recommend recipe (with [ingredient])\n"
            "- show/find/suggest recipe for/with [diet] (vegetarian, vegan, gluten-free, etc.)\n"
            "- how long/cooking time/time to cook [recipe name]\n"
            "- substitute/replacement for/what can I use instead of [ingredient]\n"
            "- tip/tips/advice/how to (for/about) [recipe or ingredient]\n"
            "- help\n"
            "- hello/hi/hey"
        )
        
    def enterGreeting(self, ctx):
        self.user_input = "You are a helpful recipe assistant. Respond to this greeting in a friendly way and mention that you can help with recipes."
        self._get_ollama_response(self.user_input)

    def _get_ollama_response(self, user_input):
        try:
            response = ollama.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {
                        'role': 'system',
                        'content': (
                            'You are a helpful recipe assistant. Provide clear, accurate, and concise responses about recipes, ingredients, cooking instructions, dietary restrictions, substitutions, and tips. '
                            'Do NOT include any reasoning, thoughts, or <think> tags in your response. Only provide the final answer for the user.'
                        )
                    },
                    {
                        'role': 'user',
                        'content': user_input
                    }
                ],
                stream=self.show_reasoning,  # Enable/disable streaming based on toggle
                options={
                    'temperature': 0.7,
                    'top_p': 0.9,
                    'num_predict': 1024,
                    # 'think': False
                }
            )
            if self.show_reasoning:
                # For streaming responses, collect all chunks
                full_response = ""
                for chunk in response:
                    if 'message' in chunk and 'content' in chunk['message']:
                        full_response += chunk['message']['content']
                self.response = full_response
            else:
                self.response = response['message']['content']
        except Exception as e:
            self.response = f"I apologize, but I'm having trouble accessing the recipe information right now. Please try again later. (Error: {str(e)})"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    show_reasoning = data.get('show_reasoning', False)
    
    # Create input stream
    input_stream = InputStream(user_input)
    
    # Create lexer and parser
    lexer = ChatLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ChatParser(token_stream)
    
    # Parse the input
    tree = parser.chat()
    
    # Create listener and walk the tree
    listener = RecipeChatListener()
    listener.show_reasoning = show_reasoning
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    return jsonify({'response': listener.response})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
