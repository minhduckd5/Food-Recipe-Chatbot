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
    },
     "beef stew": {
        "description": "A hearty and comforting beef stew slow-cooked with vegetables and savory broth.",
        "ingredients": [
            "1kg beef chuck, cut into cubes",
            "2 tbsp flour",
            "2 tbsp olive oil",
            "1 onion, chopped",
            "3 cloves garlic, minced",
            "3 carrots, sliced",
            "2 potatoes, cubed",
            "2 cups beef broth",
            "1 cup red wine (optional)",
            "2 tbsp tomato paste",
            "1 tsp thyme",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Toss beef with flour, salt, and pepper",
            "Brown beef in olive oil, then remove",
            "Sauté onion and garlic in same pot",
            "Add tomato paste, cook 1 minute",
            "Return beef, add broth, wine, vegetables, and thyme",
            "Simmer covered for 2 hours until tender"
        ],
        "cooking_time": "2 hours 30 minutes",
        "dietary_info": ["gluten-free"]
    },
    "greek salad": {
        "description": "A fresh Mediterranean salad with tomatoes, cucumbers, olives, and feta cheese.",
        "ingredients": [
            "2 cups cherry tomatoes, halved",
            "1 cucumber, sliced",
            "1/2 red onion, thinly sliced",
            "1/2 cup Kalamata olives",
            "1/2 cup feta cheese, crumbled",
            "2 tbsp olive oil",
            "1 tbsp red wine vinegar",
            "1 tsp dried oregano",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Combine vegetables and olives in a bowl",
            "Whisk olive oil, vinegar, oregano, salt, and pepper",
            "Pour dressing over salad",
            "Top with feta cheese and serve"
        ],
        "cooking_time": "10 minutes",
        "dietary_info": ["vegetarian", "gluten-free", "low-carb"]
    },
    "shakshuka": {
        "description": "A flavorful North African dish of poached eggs in spicy tomato sauce.",
        "ingredients": [
            "1 tbsp olive oil",
            "1 onion, chopped",
            "1 red bell pepper, sliced",
            "3 cloves garlic, minced",
            "1 tsp cumin",
            "1 tsp paprika",
            "1/4 tsp cayenne pepper",
            "1 can diced tomatoes",
            "4 eggs",
            "Salt and pepper to taste",
            "Fresh parsley for garnish"
        ],
        "instructions": [
            "Sauté onion, pepper, and garlic in oil",
            "Add spices and cook for 1 minute",
            "Pour in tomatoes, simmer 10 minutes",
            "Make wells in sauce and crack in eggs",
            "Cover and cook until eggs are set",
            "Garnish with parsley"
        ],
        "cooking_time": "25 minutes",
        "dietary_info": ["vegetarian", "gluten-free"]
    },
    "avocado toast": {
        "description": "A quick and nutritious breakfast with mashed avocado and optional toppings.",
        "ingredients": [
            "2 slices whole grain bread",
            "1 ripe avocado",
            "1/2 lemon, juiced",
            "Salt and pepper to taste",
            "Optional toppings: poached egg, red pepper flakes, tomato, feta"
        ],
        "instructions": [
            "Toast bread slices",
            "Mash avocado with lemon, salt, and pepper",
            "Spread on toast",
            "Add desired toppings"
        ],
        "cooking_time": "10 minutes",
        "dietary_info": ["vegetarian"]
    },
    "mushroom risotto": {
        "description": "A creamy Italian rice dish with sautéed mushrooms and parmesan cheese.",
        "ingredients": [
            "1 cup arborio rice",
            "2 tbsp olive oil",
            "1 onion, chopped",
            "2 cloves garlic, minced",
            "2 cups mushrooms, sliced",
            "4 cups vegetable broth, warmed",
            "1/2 cup white wine (optional)",
            "1/2 cup parmesan cheese, grated",
            "Salt and pepper to taste",
            "Fresh parsley"
        ],
        "instructions": [
            "Sauté onion, garlic, and mushrooms in oil",
            "Add rice, stir for 1 minute",
            "Add wine and cook until absorbed",
            "Add broth one ladle at a time, stirring often",
            "Cook until rice is creamy and tender",
            "Stir in parmesan and season",
            "Garnish with parsley"
        ],
        "cooking_time": "35 minutes",
        "dietary_info": ["vegetarian", "gluten-free"]
    },
    "fish tacos": {
        "description": "Crispy fish with fresh toppings served in soft tortillas.",
        "ingredients": [
            "400g white fish fillets (like cod or tilapia)",
            "1 cup flour or cornmeal",
            "1 tsp paprika",
            "Salt and pepper",
            "8 small tortillas",
            "1 cup shredded cabbage",
            "1/2 cup sour cream or Greek yogurt",
            "1 tbsp lime juice",
            "Chopped cilantro"
        ],
        "instructions": [
            "Season and coat fish with flour mix",
            "Pan-fry until crispy and golden",
            "Mix sour cream with lime juice for sauce",
            "Assemble tacos with fish, cabbage, sauce, and cilantro"
        ],
        "cooking_time": "25 minutes",
        "dietary_info": []
    },
    "lentil soup": {
        "description": "A warm, hearty soup made with lentils, vegetables, and spices.",
        "ingredients": [
            "1 cup lentils",
            "1 onion, chopped",
            "2 carrots, chopped",
            "2 celery stalks, chopped",
            "3 cloves garlic, minced",
            "1 can diced tomatoes",
            "4 cups vegetable broth",
            "1 tsp cumin",
            "1 tsp thyme",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Sauté onion, garlic, carrots, and celery",
            "Add tomatoes, lentils, broth, and spices",
            "Simmer until lentils are soft (30–40 minutes)",
            "Adjust seasoning and serve"
        ],
        "cooking_time": "45 minutes",
        "dietary_info": ["vegan", "gluten-free"]
    },
    "stuffed bell peppers": {
        "description": "Bell peppers filled with a savory mixture of rice, vegetables, and cheese.",
        "ingredients": [
            "4 bell peppers, tops removed and seeds cleaned",
            "1 cup cooked rice",
            "1 cup cooked beans or ground meat",
            "1 cup tomato sauce",
            "1 onion, diced",
            "1 cup shredded cheese",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Preheat oven to 375°F (190°C)",
            "Sauté onion and mix with rice, beans/meat, and sauce",
            "Stuff mixture into peppers",
            "Top with cheese and bake for 30 minutes"
        ],
        "cooking_time": "40 minutes",
        "dietary_info": ["vegetarian", "gluten-free"]
    },
    "falafel wrap": {
        "description": "Crispy falafels served in pita bread with fresh vegetables and tahini sauce.",
        "ingredients": [
            "1 cup cooked or canned chickpeas",
            "2 cloves garlic",
            "1/2 onion",
            "1/4 cup fresh parsley",
            "2 tbsp flour",
            "1 tsp cumin",
            "Salt to taste",
            "Pita bread",
            "Lettuce, tomato, cucumber",
            "Tahini sauce or yogurt sauce"
        ],
        "instructions": [
            "Blend chickpeas, garlic, onion, parsley, flour, and spices",
            "Form small balls or patties and pan-fry or bake",
            "Assemble in pita with vegetables and sauce"
        ],
        "cooking_time": "30 minutes",
        "dietary_info": ["vegan"]
    },
    "banana pancakes": {
        "description": "Fluffy, naturally sweet pancakes made with bananas and minimal ingredients.",
        "ingredients": [
            "2 ripe bananas",
            "2 eggs",
            "1/2 tsp baking powder",
            "1/2 tsp cinnamon",
            "Butter or oil for cooking",
            "Maple syrup for serving"
        ],
        "instructions": [
            "Mash bananas and mix with eggs, baking powder, and cinnamon",
            "Cook on a greased skillet until golden on both sides",
            "Serve with syrup"
        ],
        "cooking_time": "15 minutes",
        "dietary_info": ["gluten-free", "dairy-free"]
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
    "cream": ["coconut cream", "cashew cream", "silken tofu", "oat cream"],
    "yogurt": ["coconut yogurt", "soy yogurt", "cashew yogurt", "almond yogurt"],
    "pasta": ["zucchini noodles", "chickpea pasta", "lentil pasta", "gluten-free pasta"],
    "broth": ["vegetable broth", "miso broth", "mushroom broth", "bouillon cube with water"],
    "parmesan cheese": ["nutritional yeast", "vegan parmesan", "ground cashews with salt", "tofu-based cheese"],
    "bacon": ["tempeh bacon", "mushroom bacon", "coconut bacon", "seitan strips"],
    "ground meat": ["lentils", "mushrooms", "textured vegetable protein (TVP)", "crumbled tofu"],
    "mayonnaise": ["vegan mayo", "mashed avocado", "hummus", "plain yogurt"],
    "sour cream": ["cashew cream", "vegan sour cream", "coconut yogurt", "plain soy yogurt"],
    "honey": ["maple syrup", "agave nectar", "date syrup", "brown rice syrup"],
    "oil": ["applesauce (in baking)", "mashed banana", "yogurt", "avocado"]
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
        "Adjust cooking time based on your stove, oven, or equipment behavior.",
        "Use quality olive oil or finishing oils to enhance flavor before serving."
    ],
    "vegetables": [
        "Don't overcrowd the pan when stir-frying.",
        "Blanch vegetables before freezing to preserve color and texture.",
        "Store herbs in a glass of water in the fridge to keep them fresh longer.",
        "Use vegetable scraps to make homemade stock.",
        "Roast vegetables at high heat for deep caramelization.",
        "Season vegetables after cooking for better flavor control.",
        "Steam vegetables to preserve nutrients.",
        "Use acid (like lemon juice or vinegar) to brighten vegetable flavors.",
        "Cut vegetables uniformly for even cooking.",
        "Add leafy greens at the end of cooking to prevent over-wilting."
    ],
    "meat": [
        "Bring meat to room temperature before cooking.",
        "Use a meat thermometer for perfect doneness.",
        "Let meat rest after cooking to retain juices.",
        "Pat meat dry before searing for better browning.",
        "Marinate meat to add flavor and tenderize.",
        "Cut meat against the grain for more tender bites.",
        "Trim excess fat to avoid flare-ups on the grill.",
        "Brown meat before adding to stews or soups for deeper flavor."
    ],
    "pasta": [
        "Salt the pasta water generously—it should taste like the sea.",
        "Reserve some pasta water for the sauce to help it stick.",
        "Don't rinse pasta after cooking; starch helps bind the sauce.",
        "Cook pasta until al dente for the best texture.",
        "Add sauce to the pasta in the pan, not the other way around.",
        "Stir pasta occasionally to prevent sticking.",
        "Use a large pot to give pasta enough space to cook evenly.",
        "Toss cooked pasta with a little oil if storing to prevent clumping."
    ],
    "baking": [
        "Preheat the oven before starting to bake.",
        "Measure ingredients precisely—baking is a science.",
        "Don't overmix batter; it can lead to tough textures.",
        "Let baked goods cool completely before cutting.",
        "Use room temperature ingredients unless specified otherwise.",
        "Test doneness with a toothpick or skewer.",
        "Avoid opening the oven door too often—heat escapes quickly.",
        "Use parchment paper or silicone mats to prevent sticking.",
        "Rotate pans halfway through baking for even cooking."
    ],
    "soups_and_stews": [
        "Start by sautéing aromatics like onion, garlic, and celery for a flavor base.",
        "Simmer gently—don’t boil vigorously—to preserve texture and clarity.",
        "Skim fat and foam from the surface for a cleaner broth.",
        "Add delicate ingredients (like spinach or herbs) toward the end.",
        "Use homemade or low-sodium broth to better control salt levels.",
        "Let soup sit for a few hours or overnight to deepen flavors.",
        "Use an immersion blender for creamy soups directly in the pot."
    ],
    "grains_and_bowls": [
        "Rinse grains like quinoa and rice to remove bitterness or excess starch.",
        "Toast dry grains before cooking to bring out nutty flavor.",
        "Let cooked grains rest before fluffing with a fork.",
        "Use broth instead of water for more flavorful grains.",
        "Mix dressings separately and add right before serving bowls.",
        "Balance textures—add something crunchy (nuts), creamy (avocado), and fresh (herbs)."
    ],
    "dips_and_spreads": [
        "Use a food processor for smoother consistency.",
        "Let dips chill before serving for deeper flavor.",
        "Adjust seasoning after chilling—flavors mellow over time.",
        "Add a splash of acid (lemon juice or vinegar) to brighten dips.",
        "Top dips with a drizzle of oil or herbs to make them more visually appealing.",
        "Use roasted garlic for a milder, sweeter garlic flavor."
    ]
}