from flask import Flask, request, jsonify
from flask_cors import CORS
from antlr4 import *
from CompiledFile.ChatLexer import ChatLexer
from CompiledFile.ChatParser import ChatParser
from CompiledFile.ChatListener import ChatListener

app = Flask(__name__)
CORS(app)

class RecipeChatListener(ChatListener):
    def __init__(self):
        self.response = ""
        
    def enterSearch_recipe(self, ctx):
        recipe_name = ctx.recipe_name().getText()
        self.response = f"Searching for recipe: {recipe_name}"
        
    def enterGet_ingredients(self, ctx):
        recipe_name = ctx.recipe_name().getText()
        self.response = f"Here are the ingredients for {recipe_name}"
        
    def enterGet_instructions(self, ctx):
        recipe_name = ctx.recipe_name().getText()
        self.response = f"Here are the instructions for {recipe_name}"
        
    def enterHelp(self, ctx):
        self.response = "Available commands:\n" + \
                       "- search recipe for [recipe name]\n" + \
                       "- show ingredients for [recipe name]\n" + \
                       "- show instructions for [recipe name]\n" + \
                       "- help\n" + \
                       "- hello/hi/hey"
        
    def enterGreeting(self, ctx):
        self.response = "Hello! How can I help you with recipes today?"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    
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
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    return jsonify({'response': listener.response})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 