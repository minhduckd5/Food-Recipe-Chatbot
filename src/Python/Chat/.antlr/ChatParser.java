// Generated from f:/Food-Recipe-Chatbot/src/Python/Chat/Chat.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ChatParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, WORD=11, SPACE=12, WS=13;
	public static final int
		RULE_chat = 0, RULE_command = 1, RULE_search_recipe = 2, RULE_get_ingredients = 3, 
		RULE_get_instructions = 4, RULE_help = 5, RULE_greeting = 6, RULE_recipe_name = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"chat", "command", "search_recipe", "get_ingredients", "get_instructions", 
			"help", "greeting", "recipe_name"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'search'", "'recipe'", "'for'", "'show'", "'ingredients'", "'instructions'", 
			"'help'", "'hello'", "'hi'", "'hey'", null, "' '"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "WORD", 
			"SPACE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Chat.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ChatParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChatContext extends ParserRuleContext {
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public ChatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chat; }
	}

	public final ChatContext chat() throws RecognitionException {
		ChatContext _localctx = new ChatContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_chat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(16);
				command();
				}
				}
				setState(19); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1938L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public Search_recipeContext search_recipe() {
			return getRuleContext(Search_recipeContext.class,0);
		}
		public Get_ingredientsContext get_ingredients() {
			return getRuleContext(Get_ingredientsContext.class,0);
		}
		public Get_instructionsContext get_instructions() {
			return getRuleContext(Get_instructionsContext.class,0);
		}
		public HelpContext help() {
			return getRuleContext(HelpContext.class,0);
		}
		public GreetingContext greeting() {
			return getRuleContext(GreetingContext.class,0);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_command);
		try {
			setState(26);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(21);
				search_recipe();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(22);
				get_ingredients();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(23);
				get_instructions();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(24);
				help();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(25);
				greeting();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Search_recipeContext extends ParserRuleContext {
		public Recipe_nameContext recipe_name() {
			return getRuleContext(Recipe_nameContext.class,0);
		}
		public Search_recipeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_search_recipe; }
	}

	public final Search_recipeContext search_recipe() throws RecognitionException {
		Search_recipeContext _localctx = new Search_recipeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_search_recipe);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(T__0);
			setState(29);
			match(T__1);
			setState(30);
			match(T__2);
			setState(31);
			recipe_name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Get_ingredientsContext extends ParserRuleContext {
		public Recipe_nameContext recipe_name() {
			return getRuleContext(Recipe_nameContext.class,0);
		}
		public Get_ingredientsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_get_ingredients; }
	}

	public final Get_ingredientsContext get_ingredients() throws RecognitionException {
		Get_ingredientsContext _localctx = new Get_ingredientsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_get_ingredients);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(T__3);
			setState(34);
			match(T__4);
			setState(35);
			match(T__2);
			setState(36);
			recipe_name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Get_instructionsContext extends ParserRuleContext {
		public Recipe_nameContext recipe_name() {
			return getRuleContext(Recipe_nameContext.class,0);
		}
		public Get_instructionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_get_instructions; }
	}

	public final Get_instructionsContext get_instructions() throws RecognitionException {
		Get_instructionsContext _localctx = new Get_instructionsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_get_instructions);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(T__3);
			setState(39);
			match(T__5);
			setState(40);
			match(T__2);
			setState(41);
			recipe_name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HelpContext extends ParserRuleContext {
		public HelpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_help; }
	}

	public final HelpContext help() throws RecognitionException {
		HelpContext _localctx = new HelpContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_help);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GreetingContext extends ParserRuleContext {
		public GreetingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_greeting; }
	}

	public final GreetingContext greeting() throws RecognitionException {
		GreetingContext _localctx = new GreetingContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_greeting);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1792L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Recipe_nameContext extends ParserRuleContext {
		public List<TerminalNode> WORD() { return getTokens(ChatParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(ChatParser.WORD, i);
		}
		public List<TerminalNode> SPACE() { return getTokens(ChatParser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(ChatParser.SPACE, i);
		}
		public Recipe_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recipe_name; }
	}

	public final Recipe_nameContext recipe_name() throws RecognitionException {
		Recipe_nameContext _localctx = new Recipe_nameContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_recipe_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(WORD);
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SPACE) {
				{
				{
				setState(48);
				match(SPACE);
				setState(49);
				match(WORD);
				}
				}
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\r8\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0001"+
		"\u0000\u0004\u0000\u0012\b\u0000\u000b\u0000\f\u0000\u0013\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u001b\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u00073\b\u0007"+
		"\n\u0007\f\u00076\t\u0007\u0001\u0007\u0000\u0000\b\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0000\u0001\u0001\u0000\b\n5\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0002\u001a\u0001\u0000\u0000\u0000\u0004\u001c\u0001\u0000"+
		"\u0000\u0000\u0006!\u0001\u0000\u0000\u0000\b&\u0001\u0000\u0000\u0000"+
		"\n+\u0001\u0000\u0000\u0000\f-\u0001\u0000\u0000\u0000\u000e/\u0001\u0000"+
		"\u0000\u0000\u0010\u0012\u0003\u0002\u0001\u0000\u0011\u0010\u0001\u0000"+
		"\u0000\u0000\u0012\u0013\u0001\u0000\u0000\u0000\u0013\u0011\u0001\u0000"+
		"\u0000\u0000\u0013\u0014\u0001\u0000\u0000\u0000\u0014\u0001\u0001\u0000"+
		"\u0000\u0000\u0015\u001b\u0003\u0004\u0002\u0000\u0016\u001b\u0003\u0006"+
		"\u0003\u0000\u0017\u001b\u0003\b\u0004\u0000\u0018\u001b\u0003\n\u0005"+
		"\u0000\u0019\u001b\u0003\f\u0006\u0000\u001a\u0015\u0001\u0000\u0000\u0000"+
		"\u001a\u0016\u0001\u0000\u0000\u0000\u001a\u0017\u0001\u0000\u0000\u0000"+
		"\u001a\u0018\u0001\u0000\u0000\u0000\u001a\u0019\u0001\u0000\u0000\u0000"+
		"\u001b\u0003\u0001\u0000\u0000\u0000\u001c\u001d\u0005\u0001\u0000\u0000"+
		"\u001d\u001e\u0005\u0002\u0000\u0000\u001e\u001f\u0005\u0003\u0000\u0000"+
		"\u001f \u0003\u000e\u0007\u0000 \u0005\u0001\u0000\u0000\u0000!\"\u0005"+
		"\u0004\u0000\u0000\"#\u0005\u0005\u0000\u0000#$\u0005\u0003\u0000\u0000"+
		"$%\u0003\u000e\u0007\u0000%\u0007\u0001\u0000\u0000\u0000&\'\u0005\u0004"+
		"\u0000\u0000\'(\u0005\u0006\u0000\u0000()\u0005\u0003\u0000\u0000)*\u0003"+
		"\u000e\u0007\u0000*\t\u0001\u0000\u0000\u0000+,\u0005\u0007\u0000\u0000"+
		",\u000b\u0001\u0000\u0000\u0000-.\u0007\u0000\u0000\u0000.\r\u0001\u0000"+
		"\u0000\u0000/4\u0005\u000b\u0000\u000001\u0005\f\u0000\u000013\u0005\u000b"+
		"\u0000\u000020\u0001\u0000\u0000\u000036\u0001\u0000\u0000\u000042\u0001"+
		"\u0000\u0000\u000045\u0001\u0000\u0000\u00005\u000f\u0001\u0000\u0000"+
		"\u000064\u0001\u0000\u0000\u0000\u0003\u0013\u001a4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}