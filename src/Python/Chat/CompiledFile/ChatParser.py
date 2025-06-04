# Generated from Chat.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,44,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,
        1,8,1,8,1,9,1,9,3,9,78,8,9,1,9,1,9,3,9,82,8,9,1,10,1,10,1,11,1,11,
        1,12,1,12,1,12,5,12,91,8,12,10,12,12,12,94,9,12,1,13,1,13,1,13,5,
        13,99,8,13,10,13,12,13,102,9,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,0,12,1,0,1,3,1,0,5,6,2,0,3,3,7,8,2,0,5,5,10,10,2,
        0,3,3,11,13,1,0,14,15,2,0,2,3,14,14,1,0,16,18,1,0,19,21,1,0,22,25,
        2,0,5,5,26,26,1,0,28,30,105,0,29,1,0,0,0,2,43,1,0,0,0,4,45,1,0,0,
        0,6,50,1,0,0,0,8,55,1,0,0,0,10,58,1,0,0,0,12,64,1,0,0,0,14,69,1,
        0,0,0,16,72,1,0,0,0,18,75,1,0,0,0,20,83,1,0,0,0,22,85,1,0,0,0,24,
        87,1,0,0,0,26,95,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,1,0,0,
        0,31,29,1,0,0,0,31,32,1,0,0,0,32,1,1,0,0,0,33,44,3,4,2,0,34,44,3,
        6,3,0,35,44,3,8,4,0,36,44,3,10,5,0,37,44,3,12,6,0,38,44,3,14,7,0,
        39,44,3,16,8,0,40,44,3,18,9,0,41,44,3,20,10,0,42,44,3,22,11,0,43,
        33,1,0,0,0,43,34,1,0,0,0,43,35,1,0,0,0,43,36,1,0,0,0,43,37,1,0,0,
        0,43,38,1,0,0,0,43,39,1,0,0,0,43,40,1,0,0,0,43,41,1,0,0,0,43,42,
        1,0,0,0,44,3,1,0,0,0,45,46,7,0,0,0,46,47,5,4,0,0,47,48,7,1,0,0,48,
        49,3,24,12,0,49,5,1,0,0,0,50,51,7,2,0,0,51,52,5,9,0,0,52,53,7,3,
        0,0,53,54,3,24,12,0,54,7,1,0,0,0,55,56,7,4,0,0,56,57,3,24,12,0,57,
        9,1,0,0,0,58,59,7,5,0,0,59,62,5,4,0,0,60,61,5,6,0,0,61,63,3,26,13,
        0,62,60,1,0,0,0,62,63,1,0,0,0,63,11,1,0,0,0,64,65,7,6,0,0,65,66,
        5,4,0,0,66,67,7,1,0,0,67,68,5,31,0,0,68,13,1,0,0,0,69,70,7,7,0,0,
        70,71,3,24,12,0,71,15,1,0,0,0,72,73,7,8,0,0,73,74,3,26,13,0,74,17,
        1,0,0,0,75,77,7,9,0,0,76,78,7,10,0,0,77,76,1,0,0,0,77,78,1,0,0,0,
        78,81,1,0,0,0,79,82,3,24,12,0,80,82,3,26,13,0,81,79,1,0,0,0,81,80,
        1,0,0,0,81,82,1,0,0,0,82,19,1,0,0,0,83,84,5,27,0,0,84,21,1,0,0,0,
        85,86,7,11,0,0,86,23,1,0,0,0,87,92,5,32,0,0,88,89,5,33,0,0,89,91,
        5,32,0,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,
        93,25,1,0,0,0,94,92,1,0,0,0,95,100,5,32,0,0,96,97,5,33,0,0,97,99,
        5,32,0,0,98,96,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,
        0,0,101,27,1,0,0,0,102,100,1,0,0,0,7,31,43,62,77,81,92,100
    ]

class ChatParser ( Parser ):

    grammarFileName = "Chat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'search'", "'find'", "'show'", "'recipe'", 
                     "'for'", "'with'", "'list'", "'what are'", "'ingredients'", 
                     "'of'", "'how to make'", "'how do I make'", "'instructions for'", 
                     "'suggest'", "'recommend'", "'how long'", "'cooking time'", 
                     "'time to cook'", "'substitute'", "'replacement for'", 
                     "'what can I use instead of'", "'tip'", "'tips'", "'advice'", 
                     "'how to'", "'about'", "'help'", "'hello'", "'hi'", 
                     "'hey'", "<INVALID>", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DIET", "WORD", 
                      "SPACE", "WS" ]

    RULE_chat = 0
    RULE_command = 1
    RULE_search_recipe = 2
    RULE_get_ingredients = 3
    RULE_get_instructions = 4
    RULE_suggest_recipe = 5
    RULE_dietary_restriction = 6
    RULE_cooking_time = 7
    RULE_substitution = 8
    RULE_cooking_tip = 9
    RULE_help = 10
    RULE_greeting = 11
    RULE_recipe_name = 12
    RULE_ingredient_name = 13

    ruleNames =  [ "chat", "command", "search_recipe", "get_ingredients", 
                   "get_instructions", "suggest_recipe", "dietary_restriction", 
                   "cooking_time", "substitution", "cooking_tip", "help", 
                   "greeting", "recipe_name", "ingredient_name" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    DIET=31
    WORD=32
    SPACE=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ChatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.CommandContext)
            else:
                return self.getTypedRuleContext(ChatParser.CommandContext,i)


        def getRuleIndex(self):
            return ChatParser.RULE_chat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChat" ):
                listener.enterChat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChat" ):
                listener.exitChat(self)




    def chat(self):

        localctx = ChatParser.ChatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.command()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2080373134) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def search_recipe(self):
            return self.getTypedRuleContext(ChatParser.Search_recipeContext,0)


        def get_ingredients(self):
            return self.getTypedRuleContext(ChatParser.Get_ingredientsContext,0)


        def get_instructions(self):
            return self.getTypedRuleContext(ChatParser.Get_instructionsContext,0)


        def suggest_recipe(self):
            return self.getTypedRuleContext(ChatParser.Suggest_recipeContext,0)


        def dietary_restriction(self):
            return self.getTypedRuleContext(ChatParser.Dietary_restrictionContext,0)


        def cooking_time(self):
            return self.getTypedRuleContext(ChatParser.Cooking_timeContext,0)


        def substitution(self):
            return self.getTypedRuleContext(ChatParser.SubstitutionContext,0)


        def cooking_tip(self):
            return self.getTypedRuleContext(ChatParser.Cooking_tipContext,0)


        def help_(self):
            return self.getTypedRuleContext(ChatParser.HelpContext,0)


        def greeting(self):
            return self.getTypedRuleContext(ChatParser.GreetingContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = ChatParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.search_recipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.get_ingredients()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.get_instructions()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.suggest_recipe()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.dietary_restriction()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.cooking_time()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 39
                self.substitution()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 40
                self.cooking_tip()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 41
                self.help_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 42
                self.greeting()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Search_recipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recipe_name(self):
            return self.getTypedRuleContext(ChatParser.Recipe_nameContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_search_recipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearch_recipe" ):
                listener.enterSearch_recipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearch_recipe" ):
                listener.exitSearch_recipe(self)




    def search_recipe(self):

        localctx = ChatParser.Search_recipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_search_recipe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 46
            self.match(ChatParser.T__3)
            self.state = 47
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 48
            self.recipe_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Get_ingredientsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recipe_name(self):
            return self.getTypedRuleContext(ChatParser.Recipe_nameContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_get_ingredients

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_ingredients" ):
                listener.enterGet_ingredients(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_ingredients" ):
                listener.exitGet_ingredients(self)




    def get_ingredients(self):

        localctx = ChatParser.Get_ingredientsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_get_ingredients)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 392) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 51
            self.match(ChatParser.T__8)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==5 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 53
            self.recipe_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Get_instructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recipe_name(self):
            return self.getTypedRuleContext(ChatParser.Recipe_nameContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_get_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_instructions" ):
                listener.enterGet_instructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_instructions" ):
                listener.exitGet_instructions(self)




    def get_instructions(self):

        localctx = ChatParser.Get_instructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_get_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            self.recipe_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Suggest_recipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ingredient_name(self):
            return self.getTypedRuleContext(ChatParser.Ingredient_nameContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_suggest_recipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuggest_recipe" ):
                listener.enterSuggest_recipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuggest_recipe" ):
                listener.exitSuggest_recipe(self)




    def suggest_recipe(self):

        localctx = ChatParser.Suggest_recipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_suggest_recipe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 59
            self.match(ChatParser.T__3)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 60
                self.match(ChatParser.T__5)
                self.state = 61
                self.ingredient_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dietary_restrictionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIET(self):
            return self.getToken(ChatParser.DIET, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_dietary_restriction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDietary_restriction" ):
                listener.enterDietary_restriction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDietary_restriction" ):
                listener.exitDietary_restriction(self)




    def dietary_restriction(self):

        localctx = ChatParser.Dietary_restrictionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dietary_restriction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16396) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 65
            self.match(ChatParser.T__3)
            self.state = 66
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 67
            self.match(ChatParser.DIET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cooking_timeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recipe_name(self):
            return self.getTypedRuleContext(ChatParser.Recipe_nameContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_cooking_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCooking_time" ):
                listener.enterCooking_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCooking_time" ):
                listener.exitCooking_time(self)




    def cooking_time(self):

        localctx = ChatParser.Cooking_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cooking_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 70
            self.recipe_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubstitutionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ingredient_name(self):
            return self.getTypedRuleContext(ChatParser.Ingredient_nameContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_substitution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstitution" ):
                listener.enterSubstitution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstitution" ):
                listener.exitSubstitution(self)




    def substitution(self):

        localctx = ChatParser.SubstitutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_substitution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
            self.ingredient_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cooking_tipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recipe_name(self):
            return self.getTypedRuleContext(ChatParser.Recipe_nameContext,0)


        def ingredient_name(self):
            return self.getTypedRuleContext(ChatParser.Ingredient_nameContext,0)


        def getRuleIndex(self):
            return ChatParser.RULE_cooking_tip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCooking_tip" ):
                listener.enterCooking_tip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCooking_tip" ):
                listener.exitCooking_tip(self)




    def cooking_tip(self):

        localctx = ChatParser.Cooking_tipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cooking_tip)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5 or _la==26:
                self.state = 76
                _la = self._input.LA(1)
                if not(_la==5 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 79
                self.recipe_name()

            elif la_ == 2:
                self.state = 80
                self.ingredient_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HelpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ChatParser.RULE_help

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelp" ):
                listener.enterHelp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelp" ):
                listener.exitHelp(self)




    def help_(self):

        localctx = ChatParser.HelpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_help)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ChatParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GreetingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ChatParser.RULE_greeting

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreeting" ):
                listener.enterGreeting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreeting" ):
                listener.exitGreeting(self)




    def greeting(self):

        localctx = ChatParser.GreetingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_greeting)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Recipe_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.WORD)
            else:
                return self.getToken(ChatParser.WORD, i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.SPACE)
            else:
                return self.getToken(ChatParser.SPACE, i)

        def getRuleIndex(self):
            return ChatParser.RULE_recipe_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecipe_name" ):
                listener.enterRecipe_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecipe_name" ):
                listener.exitRecipe_name(self)




    def recipe_name(self):

        localctx = ChatParser.Recipe_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_recipe_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ChatParser.WORD)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 88
                self.match(ChatParser.SPACE)
                self.state = 89
                self.match(ChatParser.WORD)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ingredient_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.WORD)
            else:
                return self.getToken(ChatParser.WORD, i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.SPACE)
            else:
                return self.getToken(ChatParser.SPACE, i)

        def getRuleIndex(self):
            return ChatParser.RULE_ingredient_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIngredient_name" ):
                listener.enterIngredient_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIngredient_name" ):
                listener.exitIngredient_name(self)




    def ingredient_name(self):

        localctx = ChatParser.Ingredient_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ingredient_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ChatParser.WORD)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 96
                self.match(ChatParser.SPACE)
                self.state = 97
                self.match(ChatParser.WORD)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





