grammar Chat;

chat: sentence+;

sentence: 
	(greeting | help | show_available)
	| (command (conjunction command)*)
	| (greeting | help | show_available) (command (conjunction command)*)
	PUNCT?;

command:
	search_recipe
	| get_ingredients
	| get_instructions
	| suggest_recipe
	| dietary_restriction
	| cooking_time
	| substitution
	| cooking_tip;

conjunction: 
	'and' | 'or' | 'but' | 'then' | ',';

// Search or find a recipe
search_recipe: (
		'search'
		| 'find'
		| 'show'
		| 'get'
		| 'tell me about'
		| 'i want to know about'
	) 'recipe'? ('for' | 'with' | 'about')? recipe_name;

// Get ingredients for a recipe
get_ingredients: ('show' | 'list' | 'what are' | 'tell me') 'ingredients'? (
		'for'
		| 'of'
		| 'in'
	)? recipe_name;

// Get cooking instructions
get_instructions:
	(
		'show'
		| 'how to make'
		| 'how do i make'
		| 'instructions for'
		| 'how can i make'
		| 'how can i cook'
		| 'how do i cook'
		| 'how to cook'
		| 'steps for'
		| 'tell me how to make'
		| 'i want to make'
	) recipe_name;

// Suggest a recipe (optionally with an ingredient)
suggest_recipe: (
		'suggest'
		| 'recommend'
		| 'give me'
		| 'tell me about'
	) 'recipe'? ('with' | 'using')? ingredient_name?;

// Find recipes for dietary restrictions
dietary_restriction: ('show' | 'find' | 'suggest') 'recipe'? (
		'for'
		| 'with'
		| 'that is'
	) DIET;

// Get cooking time
cooking_time: (
		'how long'
		| 'cooking time'
		| 'time to cook'
		| 'how much time'
		| 'duration'
	) ('for' | 'to make')? recipe_name;

// Get ingredient substitutions
substitution: (
		'substitute'
		| 'replacement for'
		| 'what can i use instead of'
		| 'alternative for'
		| 'what to use instead of'
	) ingredient_name;

// Get cooking tips
cooking_tip: (
		'tip'
		| 'tips'
		| 'advice'
		| 'how to'
		| 'suggestion'
		| 'recommendation'
	) ('for' | 'about')? (recipe_name | ingredient_name)?;

// Get help
help:
	'help'
	| 'what can you do'
	| 'what do you know'
	| 'show commands'
	| 'list commands';

// Greetings
greeting:
	'hello'
	| 'hi'
	| 'hey'
	| 'greetings'
	| 'good morning'
	| 'good afternoon'
	| 'good evening';

// Show available recipes
show_available: (
		'what recipes'
		| 'show recipes'
		| 'list recipes'
		| 'what dishes'
		| 'show dishes'
		| 'list dishes'
		| 'what can you cook'
		| 'what do you know how to make'
	) ('do you have' | 'are available' | 'can you make')?;

// Recipe and ingredient names can be multiple words
recipe_name: WORD (SPACE WORD)*;
ingredient_name: WORD (SPACE WORD)*;

// Dietary restrictions
DIET:
	'vegetarian'
	| 'vegan'
	| 'gluten-free'
	| 'keto'
	| 'paleo'
	| 'low-carb'
	| 'dairy-free'
	| 'nut-free';

// Basic tokens
WORD: [a-zA-Z]+;
SPACE: ' ';
PUNCT: '?' | '.' | '!';
WS: [ \t\n\r]+ -> skip;