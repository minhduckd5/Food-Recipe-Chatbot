import random
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from antlr4 import *
from CompiledFile.ChatLexer import ChatLexer
from CompiledFile.ChatParser import ChatParser
from CompiledFile.ChatListener import ChatListener
import os
import json
from antlr4.error.ErrorListener import ErrorListener as AntlrErrorListener
from data import RECIPES, SUBSTITUTIONS, COOKING_TIPS

app = Flask(__name__, 
            static_folder='templates',
            template_folder='templates')
CORS(app)



class RecipeChatListener(ChatListener):
    def __init__(self):
        self.response = ""
        self.user_input = ""
        
    def enterSearch_recipe(self, ctx):
        recipe_name = ctx.recipe_name().getText().lower()
        if recipe_name in RECIPES:
            recipe = RECIPES[recipe_name]
            self.response = (
                f"Here's the recipe for {recipe_name.title()}:\n\n"
                f"Description: {recipe['description']}\n\n"
                f"Ingredients:\n" + "\n".join(f"- {ing}" for ing in recipe['ingredients']) + "\n\n"
                f"Instructions:\n" + "\n".join(f"{i+1}. {step}" for i, step in enumerate(recipe['instructions']))
            )
        else:
            self.response = f"I'm sorry, I don't have a recipe for {recipe_name}. Would you like me to suggest a different recipe?"
        
    def enterGet_ingredients(self, ctx):
        recipe_name = ctx.recipe_name().getText().lower()
        if recipe_name in RECIPES:
            ingredients = RECIPES[recipe_name]['ingredients']
            self.response = f"Here are the ingredients for {recipe_name.title()}:\n" + "\n".join(f"- {ing}" for ing in ingredients)
        else:
            self.response = f"I'm sorry, I don't have the ingredients list for {recipe_name}."
        
    def enterGet_instructions(self, ctx):
        recipe_name = ctx.recipe_name().getText().lower()
        if recipe_name in RECIPES:
            instructions = RECIPES[recipe_name]['instructions']
            self.response = f"Here are the instructions for {recipe_name.title()}:\n" + "\n".join(f"{i+1}. {step}" for i, step in enumerate(instructions))
        else:
            self.response = f"I'm sorry, I don't have the instructions for {recipe_name}."
        
    def enterSuggest_recipe(self, ctx):
        if ctx.ingredient_name():
            ingredient = ctx.ingredient_name().getText().lower()
            # Find recipes containing the ingredient
            matching_recipes = []
            for recipe_name, recipe in RECIPES.items():
                if any(ingredient in ing.lower() for ing in recipe['ingredients']):
                    matching_recipes.append(recipe_name)
            
            if matching_recipes:
                self.response = f"I found these recipes using {ingredient}:\n" + "\n".join(f"- {recipe.title()}" for recipe in matching_recipes)
            else:
                self.response = f"I'm sorry, I don't have any recipes using {ingredient}."
        else:
            # Suggest a random recipe
            recipe_name = random.choice(list(RECIPES.keys()))
            recipe = RECIPES[recipe_name]
            self.response = (
                f"How about trying {recipe_name.title()}?\n\n"
                f"Description: {recipe['description']}\n"
                f"Cooking time: {recipe['cooking_time']}"
            )
        
    def enterDietary_restriction(self, ctx):
        print("Debug: Full input text =>", ctx.getText())
        diet = ctx.DIET().getText().lower()
        # Find recipes matching the dietary restriction
        matching_recipes = []
        for recipe_name, recipe in RECIPES.items():
            if diet in recipe['dietary_info']:
                matching_recipes.append(recipe_name)
        
        if matching_recipes:
            self.response = f"Here are some {diet} recipes:\n" + "\n".join(f"- {recipe.title()}" for recipe in matching_recipes)
        else:
            self.response = f"I'm sorry, I don't have any {diet} recipes in my database yet."
        
    def enterCooking_time(self, ctx):
        print("Debug: Full input text =>", ctx.getText())
        recipe_name = ctx.recipe_name().getText().lower()
        if recipe_name in RECIPES:
            cooking_time = RECIPES[recipe_name]['cooking_time']
            self.response = f"The cooking time for {recipe_name.title()} is {cooking_time}."
        else:
            self.response = f"I'm sorry, I don't have the cooking time for {recipe_name}."
        
    def enterSubstitution(self, ctx):
        ingredient = ctx.ingredient_name().getText().lower()
        if ingredient in SUBSTITUTIONS:
            subs = SUBSTITUTIONS[ingredient]
            self.response = f"Here are some substitutes for {ingredient}:\n" + "\n".join(f"- {sub}" for sub in subs)
        else:
            self.response = f"I'm sorry, I don't have substitution suggestions for {ingredient}."
        
    def enterCooking_tip(self, ctx):
        name = None
        if ctx.recipe_name():
            name = ctx.recipe_name().getText().lower()
        elif ctx.ingredient_name():
            name = ctx.ingredient_name().getText().lower()

        if name:
            if name in RECIPES:
                tip = random.choice(COOKING_TIPS[name])
                self.response = f"Here's a cooking tip for the recipe '{name.title()}': {tip}"
            elif name in SUBSTITUTIONS:
                tip = random.choice(COOKING_TIPS[name])
                self.response = f"Here's a cooking tip about the ingredient '{name}': {tip}"
            else:
                self.response = f"I'm not sure if '{name}' is a recipe or an ingredient, but here's a general cooking tip: {COOKING_TIPS['general'][0]}"
        else:
            self.response = f"Here's a general cooking tip: {COOKING_TIPS['general'][0]}"
        
    def enterHelp(self, ctx):
        self.response = render_template('help.html')
        return self.response
        
    def enterGreeting(self, ctx):
        self.response = render_template('greeting.html')
        return self.response

    def enterShow_available(self, ctx):
        print("Debug: Full input text =>", ctx.getText())
        recipes = list(RECIPES.keys())
        self.response = (
            "Here are all the recipes I know how to make:\n\n" +
            "\n".join(f"- {recipe.title()}" for recipe in sorted(recipes)) +
            "\n\nYou can ask me about any of these recipes for more details!"
        )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    user_input = user_input.lower()
    
    try:
        # Create input stream
        input_stream = InputStream(user_input)
        
        # Create lexer and parser
        lexer = ChatLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ChatParser(token_stream)
        
        # Add error handling
        parser.removeErrorListeners()
        parser.addErrorListener(ErrorListener())
        
        # Parse the input
        tree = parser.chat()
        
        # Create listener and walk the tree
        listener = RecipeChatListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
        return jsonify({'response': listener.response})
    except Exception as e:
        # Print debug error to terminal
        print(f"Debug Error: {str(e)}")
        # Return user-friendly message
        return jsonify({'response': "I'm having trouble understanding that. Could you try rephrasing your question?"})

class ErrorListener(AntlrErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Print debug error to terminal
        print(f"Debug Error: Syntax error at line {line}, column {column}: {msg}")
        raise Exception(f"Syntax error at line {line}, column {column}: {msg}")

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
