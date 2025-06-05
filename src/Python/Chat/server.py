from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from antlr4 import *
from CompiledFile.ChatLexer import ChatLexer
from CompiledFile.ChatParser import ChatParser
from CompiledFile.ChatListener import ChatListener
import os
import json
from antlr4.error.ErrorListener import ErrorListener as AntlrErrorListener

app = Flask(__name__, 
            static_folder='templates',
            template_folder='templates')
CORS(app)

# Recipe database
RECIPES = {
    "chicken curry": {
        "description": "A delicious and aromatic Indian-style chicken curry with rich spices and creamy sauce.",
        "ingredients": [
            "500g chicken breast, cubed",
            "2 onions, finely chopped",
            "3 cloves garlic, minced",
            "1 inch ginger, grated",
            "2 tomatoes, chopped",
            "2 tbsp curry powder",
            "1 cup coconut milk",
            "Salt and pepper to taste",
            "Fresh coriander for garnish"
        ],
        "instructions": [
            "Heat oil in a large pan and sauté onions until golden",
            "Add garlic and ginger, cook for 1 minute",
            "Add chicken and cook until browned",
            "Stir in curry powder and cook for 2 minutes",
            "Add tomatoes and cook until softened",
            "Pour in coconut milk and simmer for 20 minutes",
            "Season with salt and pepper",
            "Garnish with fresh coriander"
        ],
        "cooking_time": "30 minutes",
        "dietary_info": ["gluten-free"]
    },
    "vegetable stir fry": {
        "description": "A quick and healthy stir-fry packed with colorful vegetables and savory sauce.",
        "ingredients": [
            "2 cups mixed vegetables (bell peppers, broccoli, carrots)",
            "2 cloves garlic, minced",
            "1 tbsp ginger, grated",
            "2 tbsp soy sauce",
            "1 tbsp sesame oil",
            "2 tbsp vegetable oil",
            "Optional: tofu or protein of choice"
        ],
        "instructions": [
            "Heat vegetable oil in a wok or large pan",
            "Add garlic and ginger, stir for 30 seconds",
            "Add vegetables and stir-fry for 5-7 minutes",
            "Pour in soy sauce and sesame oil",
            "Cook for another 2 minutes until vegetables are crisp-tender"
        ],
        "cooking_time": "15 minutes",
        "dietary_info": ["vegetarian", "vegan", "gluten-free"]
    },
    "pasta carbonara": {
        "description": "A classic Italian pasta dish with creamy egg sauce, crispy bacon, and parmesan cheese.",
        "ingredients": [
            "400g spaghetti",
            "200g pancetta or bacon, diced",
            "4 large eggs",
            "100g parmesan cheese, grated",
            "2 cloves garlic, minced",
            "Black pepper to taste",
            "Salt to taste"
        ],
        "instructions": [
            "Cook pasta according to package instructions",
            "Fry pancetta until crispy",
            "Beat eggs with parmesan and black pepper",
            "Drain pasta, reserving some cooking water",
            "Quickly mix hot pasta with egg mixture",
            "Add pancetta and mix well",
            "Add pasta water if needed for creaminess"
        ],
        "cooking_time": "20 minutes",
        "dietary_info": []
    },
    "vegetable lasagna": {
        "description": "A hearty vegetarian lasagna layered with vegetables, cheese, and pasta.",
        "ingredients": [
            "12 lasagna sheets",
            "2 cups marinara sauce",
            "2 cups ricotta cheese",
            "2 cups mozzarella cheese",
            "2 cups mixed vegetables (zucchini, eggplant, mushrooms)",
            "1 onion, diced",
            "3 cloves garlic, minced",
            "Fresh basil",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Preheat oven to 375°F (190°C)",
            "Sauté vegetables with onion and garlic",
            "Layer lasagna: sauce, pasta, vegetables, cheeses",
            "Repeat layers, ending with cheese",
            "Cover with foil and bake for 45 minutes",
            "Remove foil and bake for 15 more minutes"
        ],
        "cooking_time": "1 hour 15 minutes",
        "dietary_info": ["vegetarian"]
    },
    "chocolate cake": {
        "description": "A rich and moist chocolate cake perfect for any celebration.",
        "ingredients": [
            "2 cups all-purpose flour",
            "2 cups sugar",
            "3/4 cup cocoa powder",
            "2 tsp baking powder",
            "1.5 tsp baking soda",
            "1 tsp salt",
            "2 eggs",
            "1 cup milk",
            "1/2 cup vegetable oil",
            "2 tsp vanilla extract",
            "1 cup boiling water"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C)",
            "Mix dry ingredients in a large bowl",
            "Add eggs, milk, oil, and vanilla",
            "Beat for 2 minutes",
            "Stir in boiling water",
            "Pour into greased pans",
            "Bake for 30-35 minutes"
        ],
        "cooking_time": "45 minutes",
        "dietary_info": ["vegetarian"]
    },
    "quinoa bowl": {
        "description": "A nutritious and protein-rich bowl with quinoa, vegetables, and a delicious dressing.",
        "ingredients": [
            "1 cup quinoa",
            "2 cups vegetable broth",
            "1 cucumber, diced",
            "1 bell pepper, diced",
            "1 cup cherry tomatoes, halved",
            "1 avocado, diced",
            "1/4 cup feta cheese",
            "2 tbsp olive oil",
            "1 tbsp lemon juice",
            "Fresh herbs (mint, parsley)",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Cook quinoa in vegetable broth",
            "Let quinoa cool to room temperature",
            "Mix all vegetables in a bowl",
            "Add cooled quinoa",
            "Make dressing with olive oil and lemon juice",
            "Toss everything together",
            "Top with feta and herbs"
        ],
        "cooking_time": "25 minutes",
        "dietary_info": ["vegetarian", "gluten-free"]
    }
}

# Ingredient substitutions
SUBSTITUTIONS = {
    "milk": ["almond milk", "soy milk", "oat milk", "coconut milk"],
    "eggs": ["flax eggs", "chia eggs", "banana", "applesauce"],
    "butter": ["olive oil", "coconut oil", "margarine", "avocado"],
    "sugar": ["honey", "maple syrup", "stevia", "coconut sugar"],
    "flour": ["almond flour", "coconut flour", "rice flour", "gluten-free flour blend"],
    "meat": ["tofu", "tempeh", "seitan", "jackfruit"],
    "cheese": ["nutritional yeast", "vegan cheese", "cashew cheese", "tofu ricotta"],
    "cream": ["coconut cream", "cashew cream", "silken tofu", "oat cream"]
}

# Cooking tips
COOKING_TIPS = {
    "general": [
        "Always read the recipe completely before starting",
        "Prep all ingredients before beginning to cook",
        "Keep your knives sharp for safer and more efficient cutting",
        "Taste as you cook to adjust seasonings",
        "Let meat rest after cooking for juicier results"
    ],
    "vegetables": [
        "Don't overcrowd the pan when stir-frying",
        "Blanch vegetables before freezing to preserve color and texture",
        "Store herbs in a glass of water in the fridge to keep them fresh longer",
        "Use vegetable scraps to make homemade stock"
    ],
    "meat": [
        "Bring meat to room temperature before cooking",
        "Use a meat thermometer for perfect doneness",
        "Let meat rest after cooking to retain juices",
        "Pat meat dry before searing for better browning"
    ],
    "pasta": [
        "Salt the pasta water generously",
        "Reserve some pasta water for the sauce",
        "Don't rinse pasta after cooking",
        "Cook pasta until al dente"
    ],
    "baking": [
        "Preheat the oven before starting",
        "Measure ingredients precisely",
        "Don't overmix batter",
        "Let baked goods cool completely before cutting"
    ]
}

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
            recipe_name = list(RECIPES.keys())[0]  # For now, just suggest the first recipe
            recipe = RECIPES[recipe_name]
            self.response = (
                f"How about trying {recipe_name.title()}?\n\n"
                f"Description: {recipe['description']}\n"
                f"Cooking time: {recipe['cooking_time']}"
            )
        
    def enterDietary_restriction(self, ctx):
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
        if ctx.recipe_name():
            name = ctx.recipe_name().getText().lower()
            if name in RECIPES:
                # Get a random tip from general tips
                tip = COOKING_TIPS['general'][0]  # For now, just use the first tip
                self.response = f"Here's a cooking tip for {name.title()}: {tip}"
            else:
                self.response = f"I'm sorry, I don't have specific tips for {name}."
        elif ctx.ingredient_name():
            name = ctx.ingredient_name().getText().lower()
            if name in SUBSTITUTIONS:
                # Get a random tip from general tips
                tip = COOKING_TIPS['general'][0]  # For now, just use the first tip
                self.response = f"Here's a cooking tip about {name}: {tip}"
            else:
                self.response = f"I'm sorry, I don't have specific tips about {name}."
        else:
            # Get a random general tip
            tip = COOKING_TIPS['general'][0]  # For now, just use the first tip
            self.response = f"Here's a general cooking tip: {tip}"
        
    def enterHelp(self, ctx):
        self.response = (
            "Available commands:\n"
            "- search/find/show/get/tell me about recipe for [recipe name]\n"
            "- show/list/what are/tell me ingredients for [recipe name]\n"
            "- show/how to make/steps for [recipe name]\n"
            "- suggest/recommend/give me recipe (with [ingredient])\n"
            "- show/find/suggest recipe for/with [diet] (vegetarian, vegan, gluten-free, etc.)\n"
            "- how long/cooking time/duration for [recipe name]\n"
            "- substitute/replacement for [ingredient]\n"
            "- tip/tips/advice for [recipe or ingredient]\n"
            "- what recipes/show recipes/list recipes\n"
            "- help/what can you do\n"
            "- hello/hi/hey"
        )
        
    def enterGreeting(self, ctx):
        self.response = (
            "Hello! I'm your recipe assistant. I can help you find recipes, "
            "list ingredients, provide cooking instructions, suggest substitutions, "
            "and share cooking tips. Just let me know what you'd like to know!"
        )

    def enterShow_available(self, ctx):
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
