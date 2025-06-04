grammar Chat;

chat: (command)+ ;

command: 
    search_recipe
    | get_ingredients
    | get_instructions
    | help
    | greeting
    ;

search_recipe: 'search' 'recipe' 'for' recipe_name;
get_ingredients: 'show' 'ingredients' 'for' recipe_name;
get_instructions: 'show' 'instructions' 'for' recipe_name;
help: 'help';
greeting: 'hello' | 'hi' | 'hey';

recipe_name: WORD (SPACE WORD)*;

WORD: [a-zA-Z]+;
SPACE: ' ';
WS: [ \t\n\r]+ -> skip;
