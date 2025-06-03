// Generated from c:/Users/LENOVO/Documents/GitHub/Food-Recipe-Chatbot/src/Python/Chat/Chat.g4 by ANTLR 4.13.2
// jshint ignore: start
import antlr4 from 'antlr4';
import ChatListener from './ChatListener.js';
const serializedATN = [4,1,12,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,
2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,
1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,4,2,37,8,2,11,2,12,2,38,1,3,1,3,
1,3,1,4,1,4,1,4,1,4,1,5,1,5,3,5,50,8,5,1,5,1,5,1,5,3,5,55,8,5,1,5,3,5,58,
8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,0,0,9,0,2,4,6,8,
10,12,14,16,0,1,1,0,7,8,72,0,19,1,0,0,0,2,25,1,0,0,0,4,36,1,0,0,0,6,40,1,
0,0,0,8,43,1,0,0,0,10,57,1,0,0,0,12,59,1,0,0,0,14,62,1,0,0,0,16,68,1,0,0,
0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,
22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,3,6,3,0,26,27,3,8,4,0,27,
28,3,4,2,0,28,29,5,11,0,0,29,3,1,0,0,0,30,37,3,10,5,0,31,37,3,12,6,0,32,
37,3,14,7,0,33,37,3,16,8,0,34,37,5,9,0,0,35,37,5,10,0,0,36,30,1,0,0,0,36,
31,1,0,0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,38,
1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,0,40,41,5,9,0,0,41,42,5,10,
0,0,42,7,1,0,0,0,43,44,7,0,0,0,44,45,5,1,0,0,45,46,5,10,0,0,46,9,1,0,0,0,
47,49,5,1,0,0,48,50,5,2,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,
58,5,3,0,0,52,54,5,1,0,0,53,55,5,2,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,56,
1,0,0,0,56,58,5,4,0,0,57,47,1,0,0,0,57,52,1,0,0,0,58,11,1,0,0,0,59,60,5,
12,0,0,60,61,5,12,0,0,61,13,1,0,0,0,62,63,5,5,0,0,63,64,5,9,0,0,64,65,5,
5,0,0,65,66,3,4,2,0,66,67,5,5,0,0,67,15,1,0,0,0,68,69,5,6,0,0,69,70,5,9,
0,0,70,17,1,0,0,0,6,21,36,38,49,54,57];


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.atn.PredictionContextCache();

export default class ChatParser extends antlr4.Parser {

    static grammarFileName = "Chat.g4";
    static literalNames = [ null, "':'", "'-'", "')'", "'('", "'/'", "'@'" ];
    static symbolicNames = [ null, null, null, null, null, null, null, "SAYS", 
                             "SHOUTS", "WORD", "WHITESPACE", "NEWLINE", 
                             "TEXT" ];
    static ruleNames = [ "chat", "line", "message", "name", "command", "emoticon", 
                         "link", "color", "mention" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = ChatParser.ruleNames;
        this.literalNames = ChatParser.literalNames;
        this.symbolicNames = ChatParser.symbolicNames;
    }



	chat() {
	    let localctx = new ChatContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, ChatParser.RULE_chat);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 19; 
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 18;
	            this.line();
	            this.state = 21; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while(_la===9);
	        this.state = 23;
	        this.match(ChatParser.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	line() {
	    let localctx = new LineContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 2, ChatParser.RULE_line);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 25;
	        this.name();
	        this.state = 26;
	        this.command();
	        this.state = 27;
	        this.message();
	        this.state = 28;
	        this.match(ChatParser.NEWLINE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	message() {
	    let localctx = new MessageContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, ChatParser.RULE_message);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 36; 
	        this._errHandler.sync(this);
	        var _alt = 1;
	        do {
	        	switch (_alt) {
	        	case 1:
	        		this.state = 36;
	        		this._errHandler.sync(this);
	        		switch(this._input.LA(1)) {
	        		case 1:
	        		    this.state = 30;
	        		    this.emoticon();
	        		    break;
	        		case 12:
	        		    this.state = 31;
	        		    this.link();
	        		    break;
	        		case 5:
	        		    this.state = 32;
	        		    this.color();
	        		    break;
	        		case 6:
	        		    this.state = 33;
	        		    this.mention();
	        		    break;
	        		case 9:
	        		    this.state = 34;
	        		    this.match(ChatParser.WORD);
	        		    break;
	        		case 10:
	        		    this.state = 35;
	        		    this.match(ChatParser.WHITESPACE);
	        		    break;
	        		default:
	        		    throw new antlr4.error.NoViableAltException(this);
	        		}
	        		break;
	        	default:
	        		throw new antlr4.error.NoViableAltException(this);
	        	}
	        	this.state = 38; 
	        	this._errHandler.sync(this);
	        	_alt = this._interp.adaptivePredict(this._input,2, this._ctx);
	        } while ( _alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER );
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	name() {
	    let localctx = new NameContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, ChatParser.RULE_name);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 40;
	        this.match(ChatParser.WORD);
	        this.state = 41;
	        this.match(ChatParser.WHITESPACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	command() {
	    let localctx = new CommandContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, ChatParser.RULE_command);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 43;
	        _la = this._input.LA(1);
	        if(!(_la===7 || _la===8)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	        this.state = 44;
	        this.match(ChatParser.T__0);
	        this.state = 45;
	        this.match(ChatParser.WHITESPACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	emoticon() {
	    let localctx = new EmoticonContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, ChatParser.RULE_emoticon);
	    var _la = 0;
	    try {
	        this.state = 57;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,5,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 47;
	            this.match(ChatParser.T__0);
	            this.state = 49;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===2) {
	                this.state = 48;
	                this.match(ChatParser.T__1);
	            }

	            this.state = 51;
	            this.match(ChatParser.T__2);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 52;
	            this.match(ChatParser.T__0);
	            this.state = 54;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===2) {
	                this.state = 53;
	                this.match(ChatParser.T__1);
	            }

	            this.state = 56;
	            this.match(ChatParser.T__3);
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	link() {
	    let localctx = new LinkContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, ChatParser.RULE_link);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 59;
	        this.match(ChatParser.TEXT);
	        this.state = 60;
	        this.match(ChatParser.TEXT);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	color() {
	    let localctx = new ColorContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 14, ChatParser.RULE_color);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 62;
	        this.match(ChatParser.T__4);
	        this.state = 63;
	        this.match(ChatParser.WORD);
	        this.state = 64;
	        this.match(ChatParser.T__4);
	        this.state = 65;
	        this.message();
	        this.state = 66;
	        this.match(ChatParser.T__4);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	mention() {
	    let localctx = new MentionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 16, ChatParser.RULE_mention);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 68;
	        this.match(ChatParser.T__5);
	        this.state = 69;
	        this.match(ChatParser.WORD);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

ChatParser.EOF = antlr4.Token.EOF;
ChatParser.T__0 = 1;
ChatParser.T__1 = 2;
ChatParser.T__2 = 3;
ChatParser.T__3 = 4;
ChatParser.T__4 = 5;
ChatParser.T__5 = 6;
ChatParser.SAYS = 7;
ChatParser.SHOUTS = 8;
ChatParser.WORD = 9;
ChatParser.WHITESPACE = 10;
ChatParser.NEWLINE = 11;
ChatParser.TEXT = 12;

ChatParser.RULE_chat = 0;
ChatParser.RULE_line = 1;
ChatParser.RULE_message = 2;
ChatParser.RULE_name = 3;
ChatParser.RULE_command = 4;
ChatParser.RULE_emoticon = 5;
ChatParser.RULE_link = 6;
ChatParser.RULE_color = 7;
ChatParser.RULE_mention = 8;

class ChatContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_chat;
    }

	EOF() {
	    return this.getToken(ChatParser.EOF, 0);
	};

	line = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(LineContext);
	    } else {
	        return this.getTypedRuleContext(LineContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterChat(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitChat(this);
		}
	}


}



class LineContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_line;
    }

	name() {
	    return this.getTypedRuleContext(NameContext,0);
	};

	command() {
	    return this.getTypedRuleContext(CommandContext,0);
	};

	message() {
	    return this.getTypedRuleContext(MessageContext,0);
	};

	NEWLINE() {
	    return this.getToken(ChatParser.NEWLINE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterLine(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitLine(this);
		}
	}


}



class MessageContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_message;
    }

	emoticon = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(EmoticonContext);
	    } else {
	        return this.getTypedRuleContext(EmoticonContext,i);
	    }
	};

	link = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(LinkContext);
	    } else {
	        return this.getTypedRuleContext(LinkContext,i);
	    }
	};

	color = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ColorContext);
	    } else {
	        return this.getTypedRuleContext(ColorContext,i);
	    }
	};

	mention = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(MentionContext);
	    } else {
	        return this.getTypedRuleContext(MentionContext,i);
	    }
	};

	WORD = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(ChatParser.WORD);
	    } else {
	        return this.getToken(ChatParser.WORD, i);
	    }
	};


	WHITESPACE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(ChatParser.WHITESPACE);
	    } else {
	        return this.getToken(ChatParser.WHITESPACE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterMessage(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitMessage(this);
		}
	}


}



class NameContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_name;
    }

	WORD() {
	    return this.getToken(ChatParser.WORD, 0);
	};

	WHITESPACE() {
	    return this.getToken(ChatParser.WHITESPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterName(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitName(this);
		}
	}


}



class CommandContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_command;
    }

	WHITESPACE() {
	    return this.getToken(ChatParser.WHITESPACE, 0);
	};

	SAYS() {
	    return this.getToken(ChatParser.SAYS, 0);
	};

	SHOUTS() {
	    return this.getToken(ChatParser.SHOUTS, 0);
	};

	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterCommand(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitCommand(this);
		}
	}


}



class EmoticonContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_emoticon;
    }


	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterEmoticon(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitEmoticon(this);
		}
	}


}



class LinkContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_link;
    }

	TEXT = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(ChatParser.TEXT);
	    } else {
	        return this.getToken(ChatParser.TEXT, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterLink(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitLink(this);
		}
	}


}



class ColorContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_color;
    }

	WORD() {
	    return this.getToken(ChatParser.WORD, 0);
	};

	message() {
	    return this.getTypedRuleContext(MessageContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterColor(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitColor(this);
		}
	}


}



class MentionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = ChatParser.RULE_mention;
    }

	WORD() {
	    return this.getToken(ChatParser.WORD, 0);
	};

	enterRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.enterMention(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof ChatListener ) {
	        listener.exitMention(this);
		}
	}


}




ChatParser.ChatContext = ChatContext; 
ChatParser.LineContext = LineContext; 
ChatParser.MessageContext = MessageContext; 
ChatParser.NameContext = NameContext; 
ChatParser.CommandContext = CommandContext; 
ChatParser.EmoticonContext = EmoticonContext; 
ChatParser.LinkContext = LinkContext; 
ChatParser.ColorContext = ColorContext; 
ChatParser.MentionContext = MentionContext; 
