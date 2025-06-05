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
        4,1,76,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,3,0,33,8,0,4,0,35,8,0,11,0,12,0,36,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,3,2,54,8,2,1,
        2,3,2,57,8,2,1,2,1,2,1,3,1,3,3,3,63,8,3,1,3,3,3,66,8,3,1,3,1,3,1,
        4,1,4,1,4,1,5,1,5,3,5,75,8,5,1,5,3,5,78,8,5,1,5,3,5,81,8,5,1,6,1,
        6,3,6,85,8,6,1,6,1,6,1,6,1,7,1,7,3,7,92,8,7,1,7,1,7,1,8,1,8,1,8,
        1,9,1,9,3,9,101,8,9,1,9,1,9,3,9,105,8,9,1,10,1,10,1,11,1,11,1,12,
        1,12,3,12,113,8,12,1,13,1,13,1,13,5,13,118,8,13,10,13,12,13,121,
        9,13,1,14,1,14,1,14,5,14,126,8,14,10,14,12,14,129,9,14,1,14,0,0,
        15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,18,1,0,1,6,1,0,8,10,
        2,0,3,3,11,13,2,0,8,8,15,16,2,0,3,3,17,26,2,0,5,5,27,29,2,0,9,9,
        30,30,2,0,2,3,27,27,2,0,8,9,31,31,1,0,32,36,2,0,8,8,37,37,1,0,38,
        42,1,0,43,48,2,0,8,8,10,10,1,0,49,53,1,0,54,60,1,0,61,68,1,0,69,
        71,142,0,34,1,0,0,0,2,49,1,0,0,0,4,51,1,0,0,0,6,60,1,0,0,0,8,69,
        1,0,0,0,10,72,1,0,0,0,12,82,1,0,0,0,14,89,1,0,0,0,16,95,1,0,0,0,
        18,98,1,0,0,0,20,106,1,0,0,0,22,108,1,0,0,0,24,110,1,0,0,0,26,114,
        1,0,0,0,28,122,1,0,0,0,30,32,3,2,1,0,31,33,5,75,0,0,32,31,1,0,0,
        0,32,33,1,0,0,0,33,35,1,0,0,0,34,30,1,0,0,0,35,36,1,0,0,0,36,34,
        1,0,0,0,36,37,1,0,0,0,37,1,1,0,0,0,38,50,3,4,2,0,39,50,3,6,3,0,40,
        50,3,8,4,0,41,50,3,10,5,0,42,50,3,12,6,0,43,50,3,14,7,0,44,50,3,
        16,8,0,45,50,3,18,9,0,46,50,3,20,10,0,47,50,3,22,11,0,48,50,3,24,
        12,0,49,38,1,0,0,0,49,39,1,0,0,0,49,40,1,0,0,0,49,41,1,0,0,0,49,
        42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,49,46,1,0,0,
        0,49,47,1,0,0,0,49,48,1,0,0,0,50,3,1,0,0,0,51,53,7,0,0,0,52,54,5,
        7,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,57,7,1,0,0,56,
        55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,3,26,13,0,59,5,1,0,
        0,0,60,62,7,2,0,0,61,63,5,14,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,
        65,1,0,0,0,64,66,7,3,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,
        0,67,68,3,26,13,0,68,7,1,0,0,0,69,70,7,4,0,0,70,71,3,26,13,0,71,
        9,1,0,0,0,72,74,7,5,0,0,73,75,5,7,0,0,74,73,1,0,0,0,74,75,1,0,0,
        0,75,77,1,0,0,0,76,78,7,6,0,0,77,76,1,0,0,0,77,78,1,0,0,0,78,80,
        1,0,0,0,79,81,3,28,14,0,80,79,1,0,0,0,80,81,1,0,0,0,81,11,1,0,0,
        0,82,84,7,7,0,0,83,85,5,7,0,0,84,83,1,0,0,0,84,85,1,0,0,0,85,86,
        1,0,0,0,86,87,7,8,0,0,87,88,5,72,0,0,88,13,1,0,0,0,89,91,7,9,0,0,
        90,92,7,10,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,93,1,0,0,0,93,94,3,
        26,13,0,94,15,1,0,0,0,95,96,7,11,0,0,96,97,3,28,14,0,97,17,1,0,0,
        0,98,100,7,12,0,0,99,101,7,13,0,0,100,99,1,0,0,0,100,101,1,0,0,0,
        101,104,1,0,0,0,102,105,3,26,13,0,103,105,3,28,14,0,104,102,1,0,
        0,0,104,103,1,0,0,0,104,105,1,0,0,0,105,19,1,0,0,0,106,107,7,14,
        0,0,107,21,1,0,0,0,108,109,7,15,0,0,109,23,1,0,0,0,110,112,7,16,
        0,0,111,113,7,17,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,25,1,0,
        0,0,114,119,5,73,0,0,115,116,5,74,0,0,116,118,5,73,0,0,117,115,1,
        0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,27,1,0,
        0,0,121,119,1,0,0,0,122,127,5,73,0,0,123,124,5,74,0,0,124,126,5,
        73,0,0,125,123,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,
        0,0,0,128,29,1,0,0,0,129,127,1,0,0,0,17,32,36,49,53,56,62,65,74,
        77,80,84,91,100,104,112,119,127
    ]

class ChatParser ( Parser ):

    grammarFileName = "Chat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'search'", "'find'", "'show'", "'get'", 
                     "'tell me about'", "'i want to know about'", "'recipe'", 
                     "'for'", "'with'", "'about'", "'list'", "'what are'", 
                     "'tell me'", "'ingredients'", "'of'", "'in'", "'how to make'", 
                     "'how do i make'", "'instructions for'", "'how can i make'", 
                     "'how can i cook'", "'how do i cook'", "'how to cook'", 
                     "'steps for'", "'tell me how to make'", "'i want to make'", 
                     "'suggest'", "'recommend'", "'give me'", "'using'", 
                     "'that is'", "'how long'", "'cooking time'", "'time to cook'", 
                     "'how much time'", "'duration'", "'to make'", "'substitute'", 
                     "'replacement for'", "'what can i use instead of'", 
                     "'alternative for'", "'what to use instead of'", "'tip'", 
                     "'tips'", "'advice'", "'how to'", "'suggestion'", "'recommendation'", 
                     "'help'", "'what can you do'", "'what do you know'", 
                     "'show commands'", "'list commands'", "'hello'", "'hi'", 
                     "'hey'", "'greetings'", "'good morning'", "'good afternoon'", 
                     "'good evening'", "'what recipes'", "'show recipes'", 
                     "'list recipes'", "'what dishes'", "'show dishes'", 
                     "'list dishes'", "'what can you cook'", "'what do you know how to make'", 
                     "'do you have'", "'are available'", "'can you make'", 
                     "<INVALID>", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DIET", "WORD", "SPACE", "PUNCT", "WS" ]

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
    RULE_show_available = 12
    RULE_recipe_name = 13
    RULE_ingredient_name = 14

    ruleNames =  [ "chat", "command", "search_recipe", "get_ingredients", 
                   "get_instructions", "suggest_recipe", "dietary_restriction", 
                   "cooking_time", "substitution", "cooking_tip", "help", 
                   "greeting", "show_available", "recipe_name", "ingredient_name" ]

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
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    DIET=72
    WORD=73
    SPACE=74
    PUNCT=75
    WS=76

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


        def PUNCT(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.PUNCT)
            else:
                return self.getToken(ChatParser.PUNCT, i)

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
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.command()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==75:
                    self.state = 31
                    self.match(ChatParser.PUNCT)


                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -140660295554) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 31) != 0)):
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


        def show_available(self):
            return self.getTypedRuleContext(ChatParser.Show_availableContext,0)


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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.search_recipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.get_ingredients()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.get_instructions()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.suggest_recipe()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.dietary_restriction()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                self.cooking_time()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 44
                self.substitution()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 45
                self.cooking_tip()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 46
                self.help_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 47
                self.greeting()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 48
                self.show_available()
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
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 52
                self.match(ChatParser.T__6)


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 55
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 58
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
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 61
                self.match(ChatParser.T__13)


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 98560) != 0):
                self.state = 64
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 98560) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 67
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
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 134086664) != 0)):
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
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 73
                self.match(ChatParser.T__6)


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==30:
                self.state = 76
                _la = self._input.LA(1)
                if not(_la==9 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==73:
                self.state = 79
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
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 134217740) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 83
                self.match(ChatParser.T__6)


            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147484416) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 87
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
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133143986176) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==37:
                self.state = 90
                _la = self._input.LA(1)
                if not(_la==8 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 93
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
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8521215115264) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 96
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
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 554153860399104) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==10:
                self.state = 99
                _la = self._input.LA(1)
                if not(_la==8 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 102
                self.recipe_name()

            elif la_ == 2:
                self.state = 103
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17451448556060672) != 0)):
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
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2287828610704211968) != 0)):
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


    class Show_availableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ChatParser.RULE_show_available

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow_available" ):
                listener.enterShow_available(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow_available" ):
                listener.exitShow_available(self)




    def show_available(self):

        localctx = ChatParser.Show_availableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_show_available)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & 255) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 7) != 0):
                self.state = 111
                _la = self._input.LA(1)
                if not(((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 7) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_recipe_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ChatParser.WORD)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 115
                self.match(ChatParser.SPACE)
                self.state = 116
                self.match(ChatParser.WORD)
                self.state = 121
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
        self.enterRule(localctx, 28, self.RULE_ingredient_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ChatParser.WORD)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 123
                self.match(ChatParser.SPACE)
                self.state = 124
                self.match(ChatParser.WORD)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





