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


    # Enter a parse tree produced by ChatParser#line.
    def enterLine(self, ctx:ChatParser.LineContext):
        pass

    # Exit a parse tree produced by ChatParser#line.
    def exitLine(self, ctx:ChatParser.LineContext):
        pass



del ChatParser