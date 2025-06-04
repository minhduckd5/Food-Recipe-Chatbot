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
        4,1,13,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,1,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,51,8,7,10,7,12,7,54,9,7,1,7,0,0,
        8,0,2,4,6,8,10,12,14,0,1,1,0,8,10,53,0,17,1,0,0,0,2,26,1,0,0,0,4,
        28,1,0,0,0,6,33,1,0,0,0,8,38,1,0,0,0,10,43,1,0,0,0,12,45,1,0,0,0,
        14,47,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,
        0,0,0,19,20,1,0,0,0,20,1,1,0,0,0,21,27,3,4,2,0,22,27,3,6,3,0,23,
        27,3,8,4,0,24,27,3,10,5,0,25,27,3,12,6,0,26,21,1,0,0,0,26,22,1,0,
        0,0,26,23,1,0,0,0,26,24,1,0,0,0,26,25,1,0,0,0,27,3,1,0,0,0,28,29,
        5,1,0,0,29,30,5,2,0,0,30,31,5,3,0,0,31,32,3,14,7,0,32,5,1,0,0,0,
        33,34,5,4,0,0,34,35,5,5,0,0,35,36,5,3,0,0,36,37,3,14,7,0,37,7,1,
        0,0,0,38,39,5,4,0,0,39,40,5,6,0,0,40,41,5,3,0,0,41,42,3,14,7,0,42,
        9,1,0,0,0,43,44,5,7,0,0,44,11,1,0,0,0,45,46,7,0,0,0,46,13,1,0,0,
        0,47,52,5,11,0,0,48,49,5,12,0,0,49,51,5,11,0,0,50,48,1,0,0,0,51,
        54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,15,1,0,0,0,54,52,1,0,0,
        0,3,19,26,52
    ]

class ChatParser ( Parser ):

    grammarFileName = "Chat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'search'", "'recipe'", "'for'", "'show'", 
                     "'ingredients'", "'instructions'", "'help'", "'hello'", 
                     "'hi'", "'hey'", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WORD", "SPACE", 
                      "WS" ]

    RULE_chat = 0
    RULE_command = 1
    RULE_search_recipe = 2
    RULE_get_ingredients = 3
    RULE_get_instructions = 4
    RULE_help = 5
    RULE_greeting = 6
    RULE_recipe_name = 7

    ruleNames =  [ "chat", "command", "search_recipe", "get_ingredients", 
                   "get_instructions", "help", "greeting", "recipe_name" ]

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
    WORD=11
    SPACE=12
    WS=13

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
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.command()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1938) != 0)):
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
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.search_recipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.get_ingredients()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.get_instructions()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.help_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 25
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ChatParser.T__0)
            self.state = 29
            self.match(ChatParser.T__1)
            self.state = 30
            self.match(ChatParser.T__2)
            self.state = 31
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(ChatParser.T__3)
            self.state = 34
            self.match(ChatParser.T__4)
            self.state = 35
            self.match(ChatParser.T__2)
            self.state = 36
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ChatParser.T__3)
            self.state = 39
            self.match(ChatParser.T__5)
            self.state = 40
            self.match(ChatParser.T__2)
            self.state = 41
            self.recipe_name()
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
        self.enterRule(localctx, 10, self.RULE_help)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ChatParser.T__6)
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
        self.enterRule(localctx, 12, self.RULE_greeting)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
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
        self.enterRule(localctx, 14, self.RULE_recipe_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ChatParser.WORD)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 48
                self.match(ChatParser.SPACE)
                self.state = 49
                self.match(ChatParser.WORD)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





