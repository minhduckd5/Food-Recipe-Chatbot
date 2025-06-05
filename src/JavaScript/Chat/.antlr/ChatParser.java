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
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, T__53=54, T__54=55, T__55=56, T__56=57, T__57=58, T__58=59, 
		T__59=60, T__60=61, T__61=62, T__62=63, T__63=64, T__64=65, T__65=66, 
		T__66=67, T__67=68, T__68=69, T__69=70, T__70=71, T__71=72, T__72=73, 
		T__73=74, T__74=75, T__75=76, DIET=77, WORD=78, SPACE=79, PUNCT=80, WS=81;
	public static final int
		RULE_chat = 0, RULE_sentence = 1, RULE_command = 2, RULE_conjunction = 3, 
		RULE_search_recipe = 4, RULE_get_ingredients = 5, RULE_get_instructions = 6, 
		RULE_suggest_recipe = 7, RULE_dietary_restriction = 8, RULE_cooking_time = 9, 
		RULE_substitution = 10, RULE_cooking_tip = 11, RULE_help = 12, RULE_greeting = 13, 
		RULE_show_available = 14, RULE_recipe_name = 15, RULE_ingredient_name = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"chat", "sentence", "command", "conjunction", "search_recipe", "get_ingredients", 
			"get_instructions", "suggest_recipe", "dietary_restriction", "cooking_time", 
			"substitution", "cooking_tip", "help", "greeting", "show_available", 
			"recipe_name", "ingredient_name"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'and'", "'or'", "'but'", "'then'", "','", "'search'", "'find'", 
			"'show'", "'get'", "'tell me about'", "'i want to know about'", "'recipe'", 
			"'for'", "'with'", "'about'", "'list'", "'what are'", "'tell me'", "'ingredients'", 
			"'of'", "'in'", "'how to make'", "'how do i make'", "'instructions for'", 
			"'how can i make'", "'how can i cook'", "'how do i cook'", "'how to cook'", 
			"'steps for'", "'tell me how to make'", "'i want to make'", "'suggest'", 
			"'recommend'", "'give me'", "'using'", "'that is'", "'how long'", "'cooking time'", 
			"'time to cook'", "'how much time'", "'duration'", "'to make'", "'substitute'", 
			"'replacement for'", "'what can i use instead of'", "'alternative for'", 
			"'what to use instead of'", "'tip'", "'tips'", "'advice'", "'how to'", 
			"'suggestion'", "'recommendation'", "'help'", "'what can you do'", "'what do you know'", 
			"'show commands'", "'list commands'", "'hello'", "'hi'", "'hey'", "'greetings'", 
			"'good morning'", "'good afternoon'", "'good evening'", "'what recipes'", 
			"'show recipes'", "'list recipes'", "'what dishes'", "'show dishes'", 
			"'list dishes'", "'what can you cook'", "'what do you know how to make'", 
			"'do you have'", "'are available'", "'can you make'", null, null, "' '"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "DIET", "WORD", "SPACE", "PUNCT", "WS"
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
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
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
			setState(35); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(34);
				sentence();
				}
				}
				setState(37); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & -4501129457728L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & 1023L) != 0) );
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
	public static class SentenceContext extends ParserRuleContext {
		public GreetingContext greeting() {
			return getRuleContext(GreetingContext.class,0);
		}
		public HelpContext help() {
			return getRuleContext(HelpContext.class,0);
		}
		public Show_availableContext show_available() {
			return getRuleContext(Show_availableContext.class,0);
		}
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public List<ConjunctionContext> conjunction() {
			return getRuleContexts(ConjunctionContext.class);
		}
		public ConjunctionContext conjunction(int i) {
			return getRuleContext(ConjunctionContext.class,i);
		}
		public TerminalNode PUNCT() { return getToken(ChatParser.PUNCT, 0); }
		public SentenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentence; }
	}

	public final SentenceContext sentence() throws RecognitionException {
		SentenceContext _localctx = new SentenceContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sentence);
		int _la;
		try {
			setState(70);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(42);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__58:
				case T__59:
				case T__60:
				case T__61:
				case T__62:
				case T__63:
				case T__64:
					{
					setState(39);
					greeting();
					}
					break;
				case T__53:
				case T__54:
				case T__55:
				case T__56:
				case T__57:
					{
					setState(40);
					help();
					}
					break;
				case T__65:
				case T__66:
				case T__67:
				case T__68:
				case T__69:
				case T__70:
				case T__71:
				case T__72:
					{
					setState(41);
					show_available();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(44);
				command();
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 62L) != 0)) {
					{
					{
					setState(45);
					conjunction();
					setState(46);
					command();
					}
					}
					setState(52);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(56);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__58:
				case T__59:
				case T__60:
				case T__61:
				case T__62:
				case T__63:
				case T__64:
					{
					setState(53);
					greeting();
					}
					break;
				case T__53:
				case T__54:
				case T__55:
				case T__56:
				case T__57:
					{
					setState(54);
					help();
					}
					break;
				case T__65:
				case T__66:
				case T__67:
				case T__68:
				case T__69:
				case T__70:
				case T__71:
				case T__72:
					{
					setState(55);
					show_available();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				{
				setState(58);
				command();
				setState(64);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 62L) != 0)) {
					{
					{
					setState(59);
					conjunction();
					setState(60);
					command();
					}
					}
					setState(66);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PUNCT) {
					{
					setState(67);
					match(PUNCT);
					}
				}

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
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_command);
		try {
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				search_recipe();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
				get_ingredients();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(74);
				get_instructions();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(75);
				suggest_recipe();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(76);
				dietary_restriction();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(77);
				cooking_time();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(78);
				substitution();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(79);
				cooking_tip();
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
	public static class ConjunctionContext extends ParserRuleContext {
		public ConjunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conjunction; }
	}

	public final ConjunctionContext conjunction() throws RecognitionException {
		ConjunctionContext _localctx = new ConjunctionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_conjunction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 62L) != 0)) ) {
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
		enterRule(_localctx, 8, RULE_search_recipe);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4032L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(86);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(85);
				match(T__11);
				}
			}

			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 57344L) != 0)) {
				{
				setState(88);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 57344L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(91);
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
		enterRule(_localctx, 10, RULE_get_ingredients);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 459008L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(94);
				match(T__18);
				}
			}

			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3153920L) != 0)) {
				{
				setState(97);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3153920L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(100);
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
		enterRule(_localctx, 12, RULE_get_instructions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4290773248L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(103);
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
		enterRule(_localctx, 14, RULE_suggest_recipe);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 30064772096L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(106);
				match(T__11);
				}
			}

			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13 || _la==T__34) {
				{
				setState(109);
				_la = _input.LA(1);
				if ( !(_la==T__13 || _la==T__34) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(112);
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
		enterRule(_localctx, 16, RULE_dietary_restriction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4294967680L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(116);
				match(T__11);
				}
			}

			setState(119);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 68719501312L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(120);
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
		enterRule(_localctx, 18, RULE_cooking_time);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4260607557632L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12 || _la==T__41) {
				{
				setState(123);
				_la = _input.LA(1);
				if ( !(_la==T__12 || _la==T__41) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(126);
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
		enterRule(_localctx, 20, RULE_substitution);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 272678883688448L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(129);
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
		enterRule(_localctx, 22, RULE_cooking_tip);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 17732923532771328L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12 || _la==T__14) {
				{
				setState(132);
				_la = _input.LA(1);
				if ( !(_la==T__12 || _la==T__14) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(137);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(135);
				recipe_name();
				}
				break;
			case 2:
				{
				setState(136);
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
		enterRule(_localctx, 24, RULE_help);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 558446353793941504L) != 0)) ) {
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
	public static class GreetingContext extends ParserRuleContext {
		public GreetingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_greeting; }
	}

	public final GreetingContext greeting() throws RecognitionException {
		GreetingContext _localctx = new GreetingContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_greeting);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			_la = _input.LA(1);
			if ( !(((((_la - 59)) & ~0x3f) == 0 && ((1L << (_la - 59)) & 127L) != 0)) ) {
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
	public static class Show_availableContext extends ParserRuleContext {
		public Show_availableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_show_available; }
	}

	public final Show_availableContext show_available() throws RecognitionException {
		Show_availableContext _localctx = new Show_availableContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_show_available);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			_la = _input.LA(1);
			if ( !(((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 255L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(145);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 74)) & ~0x3f) == 0 && ((1L << (_la - 74)) & 7L) != 0)) {
				{
				setState(144);
				_la = _input.LA(1);
				if ( !(((((_la - 74)) & ~0x3f) == 0 && ((1L << (_la - 74)) & 7L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
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
		enterRule(_localctx, 30, RULE_recipe_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			match(WORD);
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SPACE) {
				{
				{
				setState(148);
				match(SPACE);
				setState(149);
				match(WORD);
				}
				}
				setState(154);
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
		enterRule(_localctx, 32, RULE_ingredient_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(WORD);
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SPACE) {
				{
				{
				setState(156);
				match(SPACE);
				setState(157);
				match(WORD);
				}
				}
				setState(162);
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
		"\u0004\u0001Q\u00a4\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0001\u0000\u0004\u0000$\b\u0000\u000b\u0000"+
		"\f\u0000%\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001+\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u00011\b\u0001\n\u0001"+
		"\f\u00014\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u00019\b\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001?\b\u0001"+
		"\n\u0001\f\u0001B\t\u0001\u0001\u0001\u0003\u0001E\b\u0001\u0003\u0001"+
		"G\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002Q\b\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0003\u0004W\b\u0004\u0001\u0004"+
		"\u0003\u0004Z\b\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0003\u0005`\b\u0005\u0001\u0005\u0003\u0005c\b\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0003"+
		"\u0007l\b\u0007\u0001\u0007\u0003\u0007o\b\u0007\u0001\u0007\u0003\u0007"+
		"r\b\u0007\u0001\b\u0001\b\u0003\bv\b\b\u0001\b\u0001\b\u0001\b\u0001\t"+
		"\u0001\t\u0003\t}\b\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0003\u000b\u0086\b\u000b\u0001\u000b\u0001\u000b\u0003\u000b"+
		"\u008a\b\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e"+
		"\u0003\u000e\u0092\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f"+
		"\u0097\b\u000f\n\u000f\f\u000f\u009a\t\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0005\u0010\u009f\b\u0010\n\u0010\f\u0010\u00a2\t\u0010\u0001\u0010"+
		"\u0000\u0000\u0011\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \u0000\u0013\u0001\u0000\u0001\u0005\u0001"+
		"\u0000\u0006\u000b\u0001\u0000\r\u000f\u0002\u0000\b\b\u0010\u0012\u0002"+
		"\u0000\r\r\u0014\u0015\u0002\u0000\b\b\u0016\u001f\u0002\u0000\n\n \""+
		"\u0002\u0000\u000e\u000e##\u0002\u0000\u0007\b  \u0002\u0000\r\u000e$"+
		"$\u0001\u0000%)\u0002\u0000\r\r**\u0001\u0000+/\u0001\u000005\u0002\u0000"+
		"\r\r\u000f\u000f\u0001\u00006:\u0001\u0000;A\u0001\u0000BI\u0001\u0000"+
		"JL\u00b2\u0000#\u0001\u0000\u0000\u0000\u0002F\u0001\u0000\u0000\u0000"+
		"\u0004P\u0001\u0000\u0000\u0000\u0006R\u0001\u0000\u0000\u0000\bT\u0001"+
		"\u0000\u0000\u0000\n]\u0001\u0000\u0000\u0000\ff\u0001\u0000\u0000\u0000"+
		"\u000ei\u0001\u0000\u0000\u0000\u0010s\u0001\u0000\u0000\u0000\u0012z"+
		"\u0001\u0000\u0000\u0000\u0014\u0080\u0001\u0000\u0000\u0000\u0016\u0083"+
		"\u0001\u0000\u0000\u0000\u0018\u008b\u0001\u0000\u0000\u0000\u001a\u008d"+
		"\u0001\u0000\u0000\u0000\u001c\u008f\u0001\u0000\u0000\u0000\u001e\u0093"+
		"\u0001\u0000\u0000\u0000 \u009b\u0001\u0000\u0000\u0000\"$\u0003\u0002"+
		"\u0001\u0000#\"\u0001\u0000\u0000\u0000$%\u0001\u0000\u0000\u0000%#\u0001"+
		"\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&\u0001\u0001\u0000\u0000"+
		"\u0000\'+\u0003\u001a\r\u0000(+\u0003\u0018\f\u0000)+\u0003\u001c\u000e"+
		"\u0000*\'\u0001\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000*)\u0001\u0000"+
		"\u0000\u0000+G\u0001\u0000\u0000\u0000,2\u0003\u0004\u0002\u0000-.\u0003"+
		"\u0006\u0003\u0000./\u0003\u0004\u0002\u0000/1\u0001\u0000\u0000\u0000"+
		"0-\u0001\u0000\u0000\u000014\u0001\u0000\u0000\u000020\u0001\u0000\u0000"+
		"\u000023\u0001\u0000\u0000\u00003G\u0001\u0000\u0000\u000042\u0001\u0000"+
		"\u0000\u000059\u0003\u001a\r\u000069\u0003\u0018\f\u000079\u0003\u001c"+
		"\u000e\u000085\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u000087\u0001"+
		"\u0000\u0000\u00009:\u0001\u0000\u0000\u0000:@\u0003\u0004\u0002\u0000"+
		";<\u0003\u0006\u0003\u0000<=\u0003\u0004\u0002\u0000=?\u0001\u0000\u0000"+
		"\u0000>;\u0001\u0000\u0000\u0000?B\u0001\u0000\u0000\u0000@>\u0001\u0000"+
		"\u0000\u0000@A\u0001\u0000\u0000\u0000AD\u0001\u0000\u0000\u0000B@\u0001"+
		"\u0000\u0000\u0000CE\u0005P\u0000\u0000DC\u0001\u0000\u0000\u0000DE\u0001"+
		"\u0000\u0000\u0000EG\u0001\u0000\u0000\u0000F*\u0001\u0000\u0000\u0000"+
		"F,\u0001\u0000\u0000\u0000F8\u0001\u0000\u0000\u0000G\u0003\u0001\u0000"+
		"\u0000\u0000HQ\u0003\b\u0004\u0000IQ\u0003\n\u0005\u0000JQ\u0003\f\u0006"+
		"\u0000KQ\u0003\u000e\u0007\u0000LQ\u0003\u0010\b\u0000MQ\u0003\u0012\t"+
		"\u0000NQ\u0003\u0014\n\u0000OQ\u0003\u0016\u000b\u0000PH\u0001\u0000\u0000"+
		"\u0000PI\u0001\u0000\u0000\u0000PJ\u0001\u0000\u0000\u0000PK\u0001\u0000"+
		"\u0000\u0000PL\u0001\u0000\u0000\u0000PM\u0001\u0000\u0000\u0000PN\u0001"+
		"\u0000\u0000\u0000PO\u0001\u0000\u0000\u0000Q\u0005\u0001\u0000\u0000"+
		"\u0000RS\u0007\u0000\u0000\u0000S\u0007\u0001\u0000\u0000\u0000TV\u0007"+
		"\u0001\u0000\u0000UW\u0005\f\u0000\u0000VU\u0001\u0000\u0000\u0000VW\u0001"+
		"\u0000\u0000\u0000WY\u0001\u0000\u0000\u0000XZ\u0007\u0002\u0000\u0000"+
		"YX\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000"+
		"\u0000[\\\u0003\u001e\u000f\u0000\\\t\u0001\u0000\u0000\u0000]_\u0007"+
		"\u0003\u0000\u0000^`\u0005\u0013\u0000\u0000_^\u0001\u0000\u0000\u0000"+
		"_`\u0001\u0000\u0000\u0000`b\u0001\u0000\u0000\u0000ac\u0007\u0004\u0000"+
		"\u0000ba\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000cd\u0001\u0000"+
		"\u0000\u0000de\u0003\u001e\u000f\u0000e\u000b\u0001\u0000\u0000\u0000"+
		"fg\u0007\u0005\u0000\u0000gh\u0003\u001e\u000f\u0000h\r\u0001\u0000\u0000"+
		"\u0000ik\u0007\u0006\u0000\u0000jl\u0005\f\u0000\u0000kj\u0001\u0000\u0000"+
		"\u0000kl\u0001\u0000\u0000\u0000ln\u0001\u0000\u0000\u0000mo\u0007\u0007"+
		"\u0000\u0000nm\u0001\u0000\u0000\u0000no\u0001\u0000\u0000\u0000oq\u0001"+
		"\u0000\u0000\u0000pr\u0003 \u0010\u0000qp\u0001\u0000\u0000\u0000qr\u0001"+
		"\u0000\u0000\u0000r\u000f\u0001\u0000\u0000\u0000su\u0007\b\u0000\u0000"+
		"tv\u0005\f\u0000\u0000ut\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000"+
		"vw\u0001\u0000\u0000\u0000wx\u0007\t\u0000\u0000xy\u0005M\u0000\u0000"+
		"y\u0011\u0001\u0000\u0000\u0000z|\u0007\n\u0000\u0000{}\u0007\u000b\u0000"+
		"\u0000|{\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}~\u0001\u0000"+
		"\u0000\u0000~\u007f\u0003\u001e\u000f\u0000\u007f\u0013\u0001\u0000\u0000"+
		"\u0000\u0080\u0081\u0007\f\u0000\u0000\u0081\u0082\u0003 \u0010\u0000"+
		"\u0082\u0015\u0001\u0000\u0000\u0000\u0083\u0085\u0007\r\u0000\u0000\u0084"+
		"\u0086\u0007\u000e\u0000\u0000\u0085\u0084\u0001\u0000\u0000\u0000\u0085"+
		"\u0086\u0001\u0000\u0000\u0000\u0086\u0089\u0001\u0000\u0000\u0000\u0087"+
		"\u008a\u0003\u001e\u000f\u0000\u0088\u008a\u0003 \u0010\u0000\u0089\u0087"+
		"\u0001\u0000\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0001\u0000\u0000\u0000\u008a\u0017\u0001\u0000\u0000\u0000\u008b\u008c"+
		"\u0007\u000f\u0000\u0000\u008c\u0019\u0001\u0000\u0000\u0000\u008d\u008e"+
		"\u0007\u0010\u0000\u0000\u008e\u001b\u0001\u0000\u0000\u0000\u008f\u0091"+
		"\u0007\u0011\u0000\u0000\u0090\u0092\u0007\u0012\u0000\u0000\u0091\u0090"+
		"\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u001d"+
		"\u0001\u0000\u0000\u0000\u0093\u0098\u0005N\u0000\u0000\u0094\u0095\u0005"+
		"O\u0000\u0000\u0095\u0097\u0005N\u0000\u0000\u0096\u0094\u0001\u0000\u0000"+
		"\u0000\u0097\u009a\u0001\u0000\u0000\u0000\u0098\u0096\u0001\u0000\u0000"+
		"\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099\u001f\u0001\u0000\u0000"+
		"\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009b\u00a0\u0005N\u0000\u0000"+
		"\u009c\u009d\u0005O\u0000\u0000\u009d\u009f\u0005N\u0000\u0000\u009e\u009c"+
		"\u0001\u0000\u0000\u0000\u009f\u00a2\u0001\u0000\u0000\u0000\u00a0\u009e"+
		"\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1!\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u0016%*28@DFPV"+
		"Y_bknqu|\u0085\u0089\u0091\u0098\u00a0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}