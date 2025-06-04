# Generated from Chat.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChatParser import ChatParser
else:
    from ChatParser import ChatParser

# This class defines a complete listener for a parse tree produced by ChatParser.
class ChatListener(ParseTreeListener):

    # Enter a parse tree produced by ChatParser#chat.
    def enterChat(self, ctx:ChatParser.ChatContext):
        pass

    # Exit a parse tree produced by ChatParser#chat.
    def exitChat(self, ctx:ChatParser.ChatContext):
        pass


    # Enter a parse tree produced by ChatParser#command.
    def enterCommand(self, ctx:ChatParser.CommandContext):
        pass

    # Exit a parse tree produced by ChatParser#command.
    def exitCommand(self, ctx:ChatParser.CommandContext):
        pass


    # Enter a parse tree produced by ChatParser#search_recipe.
    def enterSearch_recipe(self, ctx:ChatParser.Search_recipeContext):
        pass

    # Exit a parse tree produced by ChatParser#search_recipe.
    def exitSearch_recipe(self, ctx:ChatParser.Search_recipeContext):
        pass


    # Enter a parse tree produced by ChatParser#get_ingredients.
    def enterGet_ingredients(self, ctx:ChatParser.Get_ingredientsContext):
        pass

    # Exit a parse tree produced by ChatParser#get_ingredients.
    def exitGet_ingredients(self, ctx:ChatParser.Get_ingredientsContext):
        pass


    # Enter a parse tree produced by ChatParser#get_instructions.
    def enterGet_instructions(self, ctx:ChatParser.Get_instructionsContext):
        pass

    # Exit a parse tree produced by ChatParser#get_instructions.
    def exitGet_instructions(self, ctx:ChatParser.Get_instructionsContext):
        pass


    # Enter a parse tree produced by ChatParser#help.
    def enterHelp(self, ctx:ChatParser.HelpContext):
        pass

    # Exit a parse tree produced by ChatParser#help.
    def exitHelp(self, ctx:ChatParser.HelpContext):
        pass


    # Enter a parse tree produced by ChatParser#greeting.
    def enterGreeting(self, ctx:ChatParser.GreetingContext):
        pass

    # Exit a parse tree produced by ChatParser#greeting.
    def exitGreeting(self, ctx:ChatParser.GreetingContext):
        pass


    # Enter a parse tree produced by ChatParser#recipe_name.
    def enterRecipe_name(self, ctx:ChatParser.Recipe_nameContext):
        pass

    # Exit a parse tree produced by ChatParser#recipe_name.
    def exitRecipe_name(self, ctx:ChatParser.Recipe_nameContext):
        pass



del ChatParser