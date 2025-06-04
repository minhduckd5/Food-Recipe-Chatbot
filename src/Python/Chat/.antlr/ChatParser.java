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
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, DIET=35, WORD=36, SPACE=37, PUNCT=38, WS=39;
	public static final int
		RULE_chat = 0, RULE_command = 1, RULE_search_recipe = 2, RULE_get_ingredients = 3, 
		RULE_get_instructions = 4, RULE_suggest_recipe = 5, RULE_dietary_restriction = 6, 
		RULE_cooking_time = 7, RULE_substitution = 8, RULE_cooking_tip = 9, RULE_help = 10, 
		RULE_greeting = 11, RULE_recipe_name = 12, RULE_ingredient_name = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"chat", "command", "search_recipe", "get_ingredients", "get_instructions", 
			"suggest_recipe", "dietary_restriction", "cooking_time", "substitution", 
			"cooking_tip", "help", "greeting", "recipe_name", "ingredient_name"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'search'", "'find'", "'show'", "'recipe'", "'for'", "'with'", 
			"'list'", "'what are'", "'ingredients'", "'of'", "'how to make'", "'how do I make'", 
			"'instructions for'", "'how can I make'", "'how can I cook'", "'how do I cook'", 
			"'how to cook'", "'suggest'", "'recommend'", "'how long'", "'cooking time'", 
			"'time to cook'", "'substitute'", "'replacement for'", "'what can I use instead of'", 
			"'tip'", "'tips'", "'advice'", "'how to'", "'about'", "'help'", "'hello'", 
			"'hi'", "'hey'", null, null, "' '"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "DIET", 
			"WORD", "SPACE", "PUNCT", "WS"
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
		public List<TerminalNode> PUNCT() { return getTokens(ChatParser.PUNCT); }
		public TerminalNode PUNCT(int i) {
			return getToken(ChatParser.PUNCT, i);
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
			setState(32); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(28);
				command();
				setState(30);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PUNCT) {
					{
					setState(29);
					match(PUNCT);
					}
				}

				}
				}
				setState(34); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 33285994894L) != 0) );
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
		public Suggest_recipeContext suggest_recipe() {
			return getRuleContext(Suggest_recipeContext.class,0);
		}
		public Dietary_restrictionContext dietary_restriction() {
			return getRuleContext(Dietary_restrictionContext.class,0);
		}
		public Cooking_timeContext cooking_time() {
			return getRuleContext(Cooking_timeContext.class,0);
		}
		public SubstitutionContext substitution() {
			return getRuleContext(SubstitutionContext.class,0);
		}
		public Cooking_tipContext cooking_tip() {
			return getRuleContext(Cooking_tipContext.class,0);
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
			setState(46);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				search_recipe();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(37);
				get_ingredients();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(38);
				get_instructions();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(39);
				suggest_recipe();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(40);
				dietary_restriction();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(41);
				cooking_time();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(42);
				substitution();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(43);
				cooking_tip();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(44);
				help();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(45);
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 14L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(49);
			match(T__3);
			setState(50);
			_la = _input.LA(1);
			if ( !(_la==T__4 || _la==T__5) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(51);
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 392L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(54);
			match(T__8);
			setState(55);
			_la = _input.LA(1);
			if ( !(_la==T__4 || _la==T__9) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(56);
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 260104L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(59);
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
	public static class Suggest_recipeContext extends ParserRuleContext {
		public Ingredient_nameContext ingredient_name() {
			return getRuleContext(Ingredient_nameContext.class,0);
		}
		public Suggest_recipeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suggest_recipe; }
	}

	public final Suggest_recipeContext suggest_recipe() throws RecognitionException {
		Suggest_recipeContext _localctx = new Suggest_recipeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_suggest_recipe);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_la = _input.LA(1);
			if ( !(_la==T__17 || _la==T__18) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(62);
			match(T__3);
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(63);
				match(T__5);
				setState(64);
				ingredient_name();
				}
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
	public static class Dietary_restrictionContext extends ParserRuleContext {
		public TerminalNode DIET() { return getToken(ChatParser.DIET, 0); }
		public Dietary_restrictionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dietary_restriction; }
	}

	public final Dietary_restrictionContext dietary_restriction() throws RecognitionException {
		Dietary_restrictionContext _localctx = new Dietary_restrictionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_dietary_restriction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 262156L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(68);
			match(T__3);
			setState(69);
			_la = _input.LA(1);
			if ( !(_la==T__4 || _la==T__5) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(70);
			match(DIET);
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
	public static class Cooking_timeContext extends ParserRuleContext {
		public Recipe_nameContext recipe_name() {
			return getRuleContext(Recipe_nameContext.class,0);
		}
		public Cooking_timeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cooking_time; }
	}

	public final Cooking_timeContext cooking_time() throws RecognitionException {
		Cooking_timeContext _localctx = new Cooking_timeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_cooking_time);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340032L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(73);
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
	public static class SubstitutionContext extends ParserRuleContext {
		public Ingredient_nameContext ingredient_name() {
			return getRuleContext(Ingredient_nameContext.class,0);
		}
		public SubstitutionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_substitution; }
	}

	public final SubstitutionContext substitution() throws RecognitionException {
		SubstitutionContext _localctx = new SubstitutionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_substitution);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 58720256L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(76);
			ingredient_name();
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
	public static class Cooking_tipContext extends ParserRuleContext {
		public Recipe_nameContext recipe_name() {
			return getRuleContext(Recipe_nameContext.class,0);
		}
		public Ingredient_nameContext ingredient_name() {
			return getRuleContext(Ingredient_nameContext.class,0);
		}
		public Cooking_tipContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cooking_tip; }
	}

	public final Cooking_tipContext cooking_tip() throws RecognitionException {
		Cooking_tipContext _localctx = new Cooking_tipContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_cooking_tip);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1006632960L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4 || _la==T__29) {
				{
				setState(79);
				_la = _input.LA(1);
				if ( !(_la==T__4 || _la==T__29) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(84);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(82);
				recipe_name();
				}
				break;
			case 2:
				{
				setState(83);
				ingredient_name();
				}
				break;
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
	public static class HelpContext extends ParserRuleContext {
		public HelpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_help; }
	}

	public final HelpContext help() throws RecognitionException {
		HelpContext _localctx = new HelpContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_help);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(T__30);
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
		enterRule(_localctx, 22, RULE_greeting);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 30064771072L) != 0)) ) {
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
		enterRule(_localctx, 24, RULE_recipe_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(WORD);
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SPACE) {
				{
				{
				setState(91);
				match(SPACE);
				setState(92);
				match(WORD);
				}
				}
				setState(97);
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

	@SuppressWarnings("CheckReturnValue")
	public static class Ingredient_nameContext extends ParserRuleContext {
		public List<TerminalNode> WORD() { return getTokens(ChatParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(ChatParser.WORD, i);
		}
		public List<TerminalNode> SPACE() { return getTokens(ChatParser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(ChatParser.SPACE, i);
		}
		public Ingredient_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ingredient_name; }
	}

	public final Ingredient_nameContext ingredient_name() throws RecognitionException {
		Ingredient_nameContext _localctx = new Ingredient_nameContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_ingredient_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(WORD);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SPACE) {
				{
				{
				setState(99);
				match(SPACE);
				setState(100);
				match(WORD);
				}
				}
				setState(105);
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
		"\u0004\u0001\'k\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0003\u0000\u001f\b"+
		"\u0000\u0004\u0000!\b\u0000\u000b\u0000\f\u0000\"\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001/\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005B\b\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0003\tQ\b\t\u0001"+
		"\t\u0001\t\u0003\tU\b\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0005\f^\b\f\n\f\f\fa\t\f\u0001\r\u0001\r\u0001\r\u0005"+
		"\rf\b\r\n\r\f\ri\t\r\u0001\r\u0000\u0000\u000e\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u0000\f\u0001\u0000\u0001"+
		"\u0003\u0001\u0000\u0005\u0006\u0002\u0000\u0003\u0003\u0007\b\u0002\u0000"+
		"\u0005\u0005\n\n\u0002\u0000\u0003\u0003\u000b\u0011\u0001\u0000\u0012"+
		"\u0013\u0002\u0000\u0002\u0003\u0012\u0012\u0001\u0000\u0014\u0016\u0001"+
		"\u0000\u0017\u0019\u0001\u0000\u001a\u001d\u0002\u0000\u0005\u0005\u001e"+
		"\u001e\u0001\u0000 \"m\u0000 \u0001\u0000\u0000\u0000\u0002.\u0001\u0000"+
		"\u0000\u0000\u00040\u0001\u0000\u0000\u0000\u00065\u0001\u0000\u0000\u0000"+
		"\b:\u0001\u0000\u0000\u0000\n=\u0001\u0000\u0000\u0000\fC\u0001\u0000"+
		"\u0000\u0000\u000eH\u0001\u0000\u0000\u0000\u0010K\u0001\u0000\u0000\u0000"+
		"\u0012N\u0001\u0000\u0000\u0000\u0014V\u0001\u0000\u0000\u0000\u0016X"+
		"\u0001\u0000\u0000\u0000\u0018Z\u0001\u0000\u0000\u0000\u001ab\u0001\u0000"+
		"\u0000\u0000\u001c\u001e\u0003\u0002\u0001\u0000\u001d\u001f\u0005&\u0000"+
		"\u0000\u001e\u001d\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000"+
		"\u0000\u001f!\u0001\u0000\u0000\u0000 \u001c\u0001\u0000\u0000\u0000!"+
		"\"\u0001\u0000\u0000\u0000\" \u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000"+
		"\u0000#\u0001\u0001\u0000\u0000\u0000$/\u0003\u0004\u0002\u0000%/\u0003"+
		"\u0006\u0003\u0000&/\u0003\b\u0004\u0000\'/\u0003\n\u0005\u0000(/\u0003"+
		"\f\u0006\u0000)/\u0003\u000e\u0007\u0000*/\u0003\u0010\b\u0000+/\u0003"+
		"\u0012\t\u0000,/\u0003\u0014\n\u0000-/\u0003\u0016\u000b\u0000.$\u0001"+
		"\u0000\u0000\u0000.%\u0001\u0000\u0000\u0000.&\u0001\u0000\u0000\u0000"+
		".\'\u0001\u0000\u0000\u0000.(\u0001\u0000\u0000\u0000.)\u0001\u0000\u0000"+
		"\u0000.*\u0001\u0000\u0000\u0000.+\u0001\u0000\u0000\u0000.,\u0001\u0000"+
		"\u0000\u0000.-\u0001\u0000\u0000\u0000/\u0003\u0001\u0000\u0000\u0000"+
		"01\u0007\u0000\u0000\u000012\u0005\u0004\u0000\u000023\u0007\u0001\u0000"+
		"\u000034\u0003\u0018\f\u00004\u0005\u0001\u0000\u0000\u000056\u0007\u0002"+
		"\u0000\u000067\u0005\t\u0000\u000078\u0007\u0003\u0000\u000089\u0003\u0018"+
		"\f\u00009\u0007\u0001\u0000\u0000\u0000:;\u0007\u0004\u0000\u0000;<\u0003"+
		"\u0018\f\u0000<\t\u0001\u0000\u0000\u0000=>\u0007\u0005\u0000\u0000>A"+
		"\u0005\u0004\u0000\u0000?@\u0005\u0006\u0000\u0000@B\u0003\u001a\r\u0000"+
		"A?\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000B\u000b\u0001\u0000"+
		"\u0000\u0000CD\u0007\u0006\u0000\u0000DE\u0005\u0004\u0000\u0000EF\u0007"+
		"\u0001\u0000\u0000FG\u0005#\u0000\u0000G\r\u0001\u0000\u0000\u0000HI\u0007"+
		"\u0007\u0000\u0000IJ\u0003\u0018\f\u0000J\u000f\u0001\u0000\u0000\u0000"+
		"KL\u0007\b\u0000\u0000LM\u0003\u001a\r\u0000M\u0011\u0001\u0000\u0000"+
		"\u0000NP\u0007\t\u0000\u0000OQ\u0007\n\u0000\u0000PO\u0001\u0000\u0000"+
		"\u0000PQ\u0001\u0000\u0000\u0000QT\u0001\u0000\u0000\u0000RU\u0003\u0018"+
		"\f\u0000SU\u0003\u001a\r\u0000TR\u0001\u0000\u0000\u0000TS\u0001\u0000"+
		"\u0000\u0000TU\u0001\u0000\u0000\u0000U\u0013\u0001\u0000\u0000\u0000"+
		"VW\u0005\u001f\u0000\u0000W\u0015\u0001\u0000\u0000\u0000XY\u0007\u000b"+
		"\u0000\u0000Y\u0017\u0001\u0000\u0000\u0000Z_\u0005$\u0000\u0000[\\\u0005"+
		"%\u0000\u0000\\^\u0005$\u0000\u0000][\u0001\u0000\u0000\u0000^a\u0001"+
		"\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000"+
		"`\u0019\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000bg\u0005$\u0000"+
		"\u0000cd\u0005%\u0000\u0000df\u0005$\u0000\u0000ec\u0001\u0000\u0000\u0000"+
		"fi\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000"+
		"\u0000h\u001b\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000\b\u001e"+
		"\".APT_g";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}