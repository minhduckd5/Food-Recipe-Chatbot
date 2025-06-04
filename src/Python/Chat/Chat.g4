grammar Chat;

chat: (command PUNCT?)+ ;

command:
      search_recipe
    | get_ingredients
    | get_instructions
    | suggest_recipe
    | dietary_restriction
    | cooking_time
    | substitution
    | cooking_tip
    | help
    | greeting
    ;

search_recipe: ('search' | 'find' | 'show') 'recipe' ('for' | 'with') recipe_name;
get_ingredients: ('show' | 'list' | 'what are') 'ingredients' ('for' | 'of') recipe_name;
get_instructions: 
      ('show' 
    | 'how to make' 
    | 'how do I make' 
    | 'instructions for' 
    | 'how can I make' 
    | 'how can I cook' 
    | 'how do I cook' 
    | 'how to cook'
    ) recipe_name;
suggest_recipe: ('suggest' | 'recommend') 'recipe' ('with' ingredient_name)?;
dietary_restriction: ('show' | 'find' | 'suggest') 'recipe' ('for' | 'with') DIET;
cooking_time: ('how long' | 'cooking time' | 'time to cook') recipe_name;
substitution: ('substitute' | 'replacement for' | 'what can I use instead of') ingredient_name;
cooking_tip: ('tip' | 'tips' | 'advice' | 'how to') ('for' | 'about')? (recipe_name | ingredient_name)?;
help: 'help';
greeting: 'hello' | 'hi' | 'hey';

recipe_name: WORD (SPACE WORD)*;
ingredient_name: WORD (SPACE WORD)*;

DIET: 'vegetarian' | 'vegan' | 'gluten-free' | 'keto' | 'paleo' | 'low-carb';

WORD: [a-zA-Z]+;
SPACE: ' ';
PUNCT: '?' | '.' | '!';
WS: [ \t\n\r]+ -> skip;
