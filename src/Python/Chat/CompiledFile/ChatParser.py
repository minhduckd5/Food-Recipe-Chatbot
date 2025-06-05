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
        4,1,80,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,4,0,36,8,0,11,0,12,0,37,1,1,1,
        1,1,1,3,1,43,8,1,1,1,1,1,1,1,1,1,5,1,49,8,1,10,1,12,1,52,9,1,1,1,
        1,1,1,1,3,1,57,8,1,1,1,1,1,1,1,1,1,5,1,63,8,1,10,1,12,1,66,9,1,1,
        1,3,1,69,8,1,3,1,71,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,81,8,
        2,1,3,1,3,1,4,1,4,1,4,3,4,88,8,4,1,4,3,4,91,8,4,1,4,3,4,94,8,4,1,
        4,3,4,97,8,4,1,4,1,4,1,5,1,5,1,5,3,5,104,8,5,1,5,3,5,107,8,5,1,5,
        3,5,110,8,5,1,5,3,5,113,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,3,7,
        123,8,7,1,7,3,7,126,8,7,1,7,3,7,129,8,7,1,7,3,7,132,8,7,1,7,3,7,
        135,8,7,1,7,3,7,138,8,7,1,8,1,8,1,8,3,8,143,8,8,1,8,3,8,146,8,8,
        1,8,1,8,3,8,150,8,8,1,8,1,8,1,9,1,9,1,9,3,9,157,8,9,1,9,3,9,160,
        8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,3,11,170,8,11,1,11,3,11,
        173,8,11,1,11,3,11,176,8,11,1,11,1,11,3,11,180,8,11,1,12,1,12,1,
        13,1,13,1,14,1,14,1,14,3,14,189,8,14,1,15,1,15,1,15,5,15,194,8,15,
        10,15,12,15,197,9,15,1,16,1,16,1,16,5,16,202,8,16,10,16,12,16,205,
        9,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,
        19,1,0,1,5,1,0,6,11,1,0,13,15,2,0,8,8,16,18,2,0,13,13,20,21,2,0,
        8,8,22,31,2,0,10,10,32,34,2,0,14,14,35,35,2,0,7,8,32,32,2,0,13,14,
        36,36,1,0,37,41,2,0,13,13,42,42,1,0,43,47,1,0,48,53,2,0,13,13,15,
        15,1,0,54,58,1,0,59,65,3,0,22,22,56,56,66,72,1,0,73,75,233,0,35,
        1,0,0,0,2,70,1,0,0,0,4,80,1,0,0,0,6,82,1,0,0,0,8,84,1,0,0,0,10,100,
        1,0,0,0,12,116,1,0,0,0,14,120,1,0,0,0,16,139,1,0,0,0,18,153,1,0,
        0,0,20,163,1,0,0,0,22,167,1,0,0,0,24,181,1,0,0,0,26,183,1,0,0,0,
        28,185,1,0,0,0,30,190,1,0,0,0,32,198,1,0,0,0,34,36,3,2,1,0,35,34,
        1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,1,1,0,0,0,39,
        43,3,26,13,0,40,43,3,24,12,0,41,43,3,28,14,0,42,39,1,0,0,0,42,40,
        1,0,0,0,42,41,1,0,0,0,43,71,1,0,0,0,44,50,3,4,2,0,45,46,3,6,3,0,
        46,47,3,4,2,0,47,49,1,0,0,0,48,45,1,0,0,0,49,52,1,0,0,0,50,48,1,
        0,0,0,50,51,1,0,0,0,51,71,1,0,0,0,52,50,1,0,0,0,53,57,3,26,13,0,
        54,57,3,24,12,0,55,57,3,28,14,0,56,53,1,0,0,0,56,54,1,0,0,0,56,55,
        1,0,0,0,57,58,1,0,0,0,58,64,3,4,2,0,59,60,3,6,3,0,60,61,3,4,2,0,
        61,63,1,0,0,0,62,59,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,
        0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,67,69,5,79,0,0,68,67,1,0,0,0,68,
        69,1,0,0,0,69,71,1,0,0,0,70,42,1,0,0,0,70,44,1,0,0,0,70,56,1,0,0,
        0,71,3,1,0,0,0,72,81,3,8,4,0,73,81,3,10,5,0,74,81,3,12,6,0,75,81,
        3,14,7,0,76,81,3,16,8,0,77,81,3,18,9,0,78,81,3,20,10,0,79,81,3,22,
        11,0,80,72,1,0,0,0,80,73,1,0,0,0,80,74,1,0,0,0,80,75,1,0,0,0,80,
        76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,5,1,0,0,
        0,82,83,7,0,0,0,83,7,1,0,0,0,84,85,7,1,0,0,85,87,5,78,0,0,86,88,
        5,12,0,0,87,86,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,91,5,78,0,
        0,90,89,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,94,7,2,0,0,93,92,
        1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,97,5,78,0,0,96,95,1,0,0,0,
        96,97,1,0,0,0,97,98,1,0,0,0,98,99,3,30,15,0,99,9,1,0,0,0,100,101,
        7,3,0,0,101,103,5,78,0,0,102,104,5,19,0,0,103,102,1,0,0,0,103,104,
        1,0,0,0,104,106,1,0,0,0,105,107,5,78,0,0,106,105,1,0,0,0,106,107,
        1,0,0,0,107,109,1,0,0,0,108,110,7,4,0,0,109,108,1,0,0,0,109,110,
        1,0,0,0,110,112,1,0,0,0,111,113,5,78,0,0,112,111,1,0,0,0,112,113,
        1,0,0,0,113,114,1,0,0,0,114,115,3,30,15,0,115,11,1,0,0,0,116,117,
        7,5,0,0,117,118,5,78,0,0,118,119,3,30,15,0,119,13,1,0,0,0,120,122,
        7,6,0,0,121,123,5,78,0,0,122,121,1,0,0,0,122,123,1,0,0,0,123,125,
        1,0,0,0,124,126,5,12,0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,128,
        1,0,0,0,127,129,5,78,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,131,
        1,0,0,0,130,132,7,7,0,0,131,130,1,0,0,0,131,132,1,0,0,0,132,134,
        1,0,0,0,133,135,5,78,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,137,
        1,0,0,0,136,138,3,32,16,0,137,136,1,0,0,0,137,138,1,0,0,0,138,15,
        1,0,0,0,139,140,7,8,0,0,140,142,5,78,0,0,141,143,5,12,0,0,142,141,
        1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,146,5,78,0,0,145,144,
        1,0,0,0,145,146,1,0,0,0,146,147,1,0,0,0,147,149,7,9,0,0,148,150,
        5,78,0,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,
        5,76,0,0,152,17,1,0,0,0,153,154,7,10,0,0,154,156,5,78,0,0,155,157,
        7,11,0,0,156,155,1,0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,160,
        5,78,0,0,159,158,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,162,
        3,30,15,0,162,19,1,0,0,0,163,164,7,12,0,0,164,165,5,78,0,0,165,166,
        3,32,16,0,166,21,1,0,0,0,167,169,7,13,0,0,168,170,5,78,0,0,169,168,
        1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,173,7,14,0,0,172,171,
        1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,176,5,78,0,0,175,174,
        1,0,0,0,175,176,1,0,0,0,176,179,1,0,0,0,177,180,3,30,15,0,178,180,
        3,32,16,0,179,177,1,0,0,0,179,178,1,0,0,0,179,180,1,0,0,0,180,23,
        1,0,0,0,181,182,7,15,0,0,182,25,1,0,0,0,183,184,7,16,0,0,184,27,
        1,0,0,0,185,186,7,17,0,0,186,188,5,78,0,0,187,189,7,18,0,0,188,187,
        1,0,0,0,188,189,1,0,0,0,189,29,1,0,0,0,190,195,5,77,0,0,191,192,
        5,78,0,0,192,194,5,77,0,0,193,191,1,0,0,0,194,197,1,0,0,0,195,193,
        1,0,0,0,195,196,1,0,0,0,196,31,1,0,0,0,197,195,1,0,0,0,198,203,5,
        77,0,0,199,200,5,78,0,0,200,202,5,77,0,0,201,199,1,0,0,0,202,205,
        1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,33,1,0,0,0,205,203,1,
        0,0,0,34,37,42,50,56,64,68,70,80,87,90,93,96,103,106,109,112,122,
        125,128,131,134,137,142,145,149,156,159,169,172,175,179,188,195,
        203
    ]

class ChatParser ( Parser ):

    grammarFileName = "Chat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'but'", "'then'", "','", 
                     "'search'", "'find'", "'show'", "'get'", "'tell me about'", 
                     "'i want to know about'", "'recipe'", "'for'", "'with'", 
                     "'about'", "'list'", "'what are'", "'tell me'", "'ingredients'", 
                     "'of'", "'in'", "'how to make'", "'how do i make'", 
                     "'instructions for'", "'how can i make'", "'how can i cook'", 
                     "'how do i cook'", "'how to cook'", "'steps for'", 
                     "'tell me how to make'", "'i want to make'", "'suggest'", 
                     "'recommend'", "'give me'", "'using'", "'that is'", 
                     "'how long'", "'cooking time'", "'time to cook'", "'how much time'", 
                     "'duration'", "'to make'", "'substitute'", "'replacement for'", 
                     "'what can i use instead of'", "'alternative for'", 
                     "'what to use instead of'", "'tip'", "'tips'", "'advice'", 
                     "'how to'", "'suggestion'", "'recommendation'", "'help'", 
                     "'what can you do'", "'what do you know'", "'show commands'", 
                     "'list commands'", "'hello'", "'hi'", "'hey'", "'greetings'", 
                     "'good morning'", "'good afternoon'", "'good evening'", 
                     "'what recipes'", "'show recipes'", "'list recipes'", 
                     "'what dishes'", "'show dishes'", "'list dishes'", 
                     "'what can you cook'", "'do you have'", "'are available'", 
                     "'can you make'", "<INVALID>", "<INVALID>", "' '" ]

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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DIET", "WORD", "SPACE", "PUNCT", "WS" ]

    RULE_chat = 0
    RULE_sentence = 1
    RULE_command = 2
    RULE_conjunction = 3
    RULE_search_recipe = 4
    RULE_get_ingredients = 5
    RULE_get_instructions = 6
    RULE_suggest_recipe = 7
    RULE_dietary_restriction = 8
    RULE_cooking_time = 9
    RULE_substitution = 10
    RULE_cooking_tip = 11
    RULE_help = 12
    RULE_greeting = 13
    RULE_show_available = 14
    RULE_recipe_name = 15
    RULE_ingredient_name = 16

    ruleNames =  [ "chat", "sentence", "command", "conjunction", "search_recipe", 
                   "get_ingredients", "get_instructions", "suggest_recipe", 
                   "dietary_restriction", "cooking_time", "substitution", 
                   "cooking_tip", "help", "greeting", "show_available", 
                   "recipe_name", "ingredient_name" ]

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
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    DIET=76
    WORD=77
    SPACE=78
    PUNCT=79
    WS=80

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

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.SentenceContext)
            else:
                return self.getTypedRuleContext(ChatParser.SentenceContext,i)


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
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.sentence()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -4501129457728) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 511) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def greeting(self):
            return self.getTypedRuleContext(ChatParser.GreetingContext,0)


        def help_(self):
            return self.getTypedRuleContext(ChatParser.HelpContext,0)


        def show_available(self):
            return self.getTypedRuleContext(ChatParser.Show_availableContext,0)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.CommandContext)
            else:
                return self.getTypedRuleContext(ChatParser.CommandContext,i)


        def conjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChatParser.ConjunctionContext)
            else:
                return self.getTypedRuleContext(ChatParser.ConjunctionContext,i)


        def PUNCT(self):
            return self.getToken(ChatParser.PUNCT, 0)

        def getRuleIndex(self):
            return ChatParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = ChatParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 39
                    self.greeting()
                    pass

                elif la_ == 2:
                    self.state = 40
                    self.help_()
                    pass

                elif la_ == 3:
                    self.state = 41
                    self.show_available()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.command()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0):
                    self.state = 45
                    self.conjunction()
                    self.state = 46
                    self.command()
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 53
                    self.greeting()
                    pass

                elif la_ == 2:
                    self.state = 54
                    self.help_()
                    pass

                elif la_ == 3:
                    self.state = 55
                    self.show_available()
                    pass


                self.state = 58
                self.command()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0):
                    self.state = 59
                    self.conjunction()
                    self.state = 60
                    self.command()
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==79:
                    self.state = 67
                    self.match(ChatParser.PUNCT)


                pass


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
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.search_recipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.get_ingredients()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.get_instructions()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.suggest_recipe()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.dietary_restriction()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.cooking_time()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.substitution()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 79
                self.cooking_tip()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ChatParser.RULE_conjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)




    def conjunction(self):

        localctx = ChatParser.ConjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
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


    class Search_recipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.SPACE)
            else:
                return self.getToken(ChatParser.SPACE, i)

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
        self.enterRule(localctx, 8, self.RULE_search_recipe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 85
            self.match(ChatParser.SPACE)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 86
                self.match(ChatParser.T__11)


            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(ChatParser.SPACE)


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0):
                self.state = 92
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 95
                self.match(ChatParser.SPACE)


            self.state = 98
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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.SPACE)
            else:
                return self.getToken(ChatParser.SPACE, i)

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
        self.enterRule(localctx, 10, self.RULE_get_ingredients)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 459008) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 101
            self.match(ChatParser.SPACE)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 102
                self.match(ChatParser.T__18)


            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 105
                self.match(ChatParser.SPACE)


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3153920) != 0):
                self.state = 108
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3153920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 111
                self.match(ChatParser.SPACE)


            self.state = 114
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

        def SPACE(self):
            return self.getToken(ChatParser.SPACE, 0)

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
        self.enterRule(localctx, 12, self.RULE_get_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4290773248) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 117
            self.match(ChatParser.SPACE)
            self.state = 118
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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.SPACE)
            else:
                return self.getToken(ChatParser.SPACE, i)

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
        self.enterRule(localctx, 14, self.RULE_suggest_recipe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064772096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 121
                self.match(ChatParser.SPACE)


            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 124
                self.match(ChatParser.T__11)


            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 127
                self.match(ChatParser.SPACE)


            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14 or _la==35:
                self.state = 130
                _la = self._input.LA(1)
                if not(_la==14 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 133
                self.match(ChatParser.SPACE)


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==77:
                self.state = 136
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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.SPACE)
            else:
                return self.getToken(ChatParser.SPACE, i)

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
        self.enterRule(localctx, 16, self.RULE_dietary_restriction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4294967680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 140
            self.match(ChatParser.SPACE)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 141
                self.match(ChatParser.T__11)


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 144
                self.match(ChatParser.SPACE)


            self.state = 147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68719501312) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 148
                self.match(ChatParser.SPACE)


            self.state = 151
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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.SPACE)
            else:
                return self.getToken(ChatParser.SPACE, i)

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
        self.enterRule(localctx, 18, self.RULE_cooking_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4260607557632) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 154
            self.match(ChatParser.SPACE)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13 or _la==42:
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==13 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 158
                self.match(ChatParser.SPACE)


            self.state = 161
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

        def SPACE(self):
            return self.getToken(ChatParser.SPACE, 0)

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
        self.enterRule(localctx, 20, self.RULE_substitution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 272678883688448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self.match(ChatParser.SPACE)
            self.state = 165
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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChatParser.SPACE)
            else:
                return self.getToken(ChatParser.SPACE, i)

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
        self.enterRule(localctx, 22, self.RULE_cooking_tip)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17732923532771328) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 168
                self.match(ChatParser.SPACE)


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13 or _la==15:
                self.state = 171
                _la = self._input.LA(1)
                if not(_la==13 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 174
                self.match(ChatParser.SPACE)


            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 177
                self.recipe_name()

            elif la_ == 2:
                self.state = 178
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
        self.enterRule(localctx, 24, self.RULE_help)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 558446353793941504) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_greeting)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not(((((_la - 59)) & ~0x3f) == 0 and ((1 << (_la - 59)) & 127) != 0)):
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

        def SPACE(self):
            return self.getToken(ChatParser.SPACE, 0)

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
        self.enterRule(localctx, 28, self.RULE_show_available)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not(((((_la - 22)) & ~0x3f) == 0 and ((1 << (_la - 22)) & 2234224807510017) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 186
            self.match(ChatParser.SPACE)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 7) != 0):
                self.state = 187
                _la = self._input.LA(1)
                if not(((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 7) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_recipe_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(ChatParser.WORD)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==78:
                self.state = 191
                self.match(ChatParser.SPACE)
                self.state = 192
                self.match(ChatParser.WORD)
                self.state = 197
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
        self.enterRule(localctx, 32, self.RULE_ingredient_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(ChatParser.WORD)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==78:
                self.state = 199
                self.match(ChatParser.SPACE)
                self.state = 200
                self.match(ChatParser.WORD)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





