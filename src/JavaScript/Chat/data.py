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

COOKING_TIPS = {
    "general": [
        "Always read the recipe completely before starting.",
        "Prep all ingredients before beginning to cook.",
        "Keep your knives sharp for safer and more efficient cutting.",
        "Taste as you cook to adjust seasonings.",
        "Let meat rest after cooking for juicier results.",
        "Clean as you go to keep your workspace tidy.",
        "Use a timer to avoid overcooking or undercooking food.",
        "Organize your tools and ingredients before you start (mise en place).",
        "Use fresh herbs and spices for better flavor.",
        "Adjust cooking time based on your stove, oven, or equipment behavior."
    ],
    "vegetables": [
        "Don't overcrowd the pan when stir-frying.",
        "Blanch vegetables before freezing to preserve color and texture.",
        "Store herbs in a glass of water in the fridge to keep them fresh longer.",
        "Use vegetable scraps to make homemade stock.",
        "Roast vegetables at high heat for deep caramelization.",
        "Season vegetables after cooking for better flavor control.",
        "Steam vegetables to preserve nutrients.",
        "Use acid (like lemon juice or vinegar) to brighten vegetable flavors."
    ],
    "meat": [
        "Bring meat to room temperature before cooking.",
        "Use a meat thermometer for perfect doneness.",
        "Let meat rest after cooking to retain juices.",
        "Pat meat dry before searing for better browning.",
        "Marinate meat to add flavor and tenderize.",
        "Cut meat against the grain for more tender bites.",
        "Trim excess fat to avoid flare-ups on the grill."
    ],
    "pasta": [
        "Salt the pasta water generously—it should taste like the sea.",
        "Reserve some pasta water for the sauce to help it stick.",
        "Don't rinse pasta after cooking; starch helps bind the sauce.",
        "Cook pasta until al dente for the best texture.",
        "Add sauce to the pasta in the pan, not the other way around.",
        "Stir pasta occasionally to prevent sticking.",
        "Use a large pot to give pasta enough space to cook evenly."
    ],
    "baking": [
        "Preheat the oven before starting to bake.",
        "Measure ingredients precisely—baking is a science.",
        "Don't overmix batter; it can lead to tough textures.",
        "Let baked goods cool completely before cutting.",
        "Use room temperature ingredients unless specified otherwise.",
        "Test doneness with a toothpick or skewer.",
        "Avoid opening the oven door too often—heat escapes quickly.",
        "Use parchment paper or silicone mats to prevent sticking."
    ]
}