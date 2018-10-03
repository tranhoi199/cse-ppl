// Generated from MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MPParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INTLIT=1, LB=2, RB=3, SEMI=4, COLON=5, WS=6, PROCEDURE=7, FUNCTION=8, 
		BEGIN=9, END=10, INTTYPE=11, ID=12, ERROR_CHAR=13;
	public static final int
		RULE_program = 0, RULE_decl = 1, RULE_procdecl = 2, RULE_funcdecl = 3, 
		RULE_body = 4, RULE_stmt = 5, RULE_funcall = 6, RULE_exp = 7, RULE_mtype = 8;
	public static final String[] ruleNames = {
		"program", "decl", "procdecl", "funcdecl", "body", "stmt", "funcall", 
		"exp", "mtype"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, "'('", "')'", "';'", "':'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "INTLIT", "LB", "RB", "SEMI", "COLON", "WS", "PROCEDURE", "FUNCTION", 
		"BEGIN", "END", "INTTYPE", "ID", "ERROR_CHAR"
	};
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
	public String getGrammarFileName() { return "MP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MPParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MPParser.EOF, 0); }
		public List<DeclContext> decl() {
			return getRuleContexts(DeclContext.class);
		}
		public DeclContext decl(int i) {
			return getRuleContext(DeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(18);
				decl();
				}
				}
				setState(21); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==PROCEDURE || _la==FUNCTION );
			setState(23);
			match(EOF);
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

	public static class DeclContext extends ParserRuleContext {
		public FuncdeclContext funcdecl() {
			return getRuleContext(FuncdeclContext.class,0);
		}
		public ProcdeclContext procdecl() {
			return getRuleContext(ProcdeclContext.class,0);
		}
		public DeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitDecl(this);
		}
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_decl);
		try {
			setState(27);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNCTION:
				enterOuterAlt(_localctx, 1);
				{
				setState(25);
				funcdecl();
				}
				break;
			case PROCEDURE:
				enterOuterAlt(_localctx, 2);
				{
				setState(26);
				procdecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class ProcdeclContext extends ParserRuleContext {
		public TerminalNode PROCEDURE() { return getToken(MPParser.PROCEDURE, 0); }
		public TerminalNode ID() { return getToken(MPParser.ID, 0); }
		public TerminalNode LB() { return getToken(MPParser.LB, 0); }
		public TerminalNode RB() { return getToken(MPParser.RB, 0); }
		public TerminalNode SEMI() { return getToken(MPParser.SEMI, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ProcdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterProcdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitProcdecl(this);
		}
	}

	public final ProcdeclContext procdecl() throws RecognitionException {
		ProcdeclContext _localctx = new ProcdeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_procdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29);
			match(PROCEDURE);
			setState(30);
			match(ID);
			setState(31);
			match(LB);
			setState(32);
			match(RB);
			setState(33);
			match(SEMI);
			setState(34);
			body();
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

	public static class FuncdeclContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(MPParser.FUNCTION, 0); }
		public TerminalNode ID() { return getToken(MPParser.ID, 0); }
		public TerminalNode LB() { return getToken(MPParser.LB, 0); }
		public TerminalNode RB() { return getToken(MPParser.RB, 0); }
		public TerminalNode COLON() { return getToken(MPParser.COLON, 0); }
		public MtypeContext mtype() {
			return getRuleContext(MtypeContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MPParser.SEMI, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public FuncdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterFuncdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitFuncdecl(this);
		}
	}

	public final FuncdeclContext funcdecl() throws RecognitionException {
		FuncdeclContext _localctx = new FuncdeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_funcdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(FUNCTION);
			setState(37);
			match(ID);
			setState(38);
			match(LB);
			setState(39);
			match(RB);
			setState(40);
			match(COLON);
			setState(41);
			mtype();
			setState(42);
			match(SEMI);
			setState(43);
			body();
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

	public static class BodyContext extends ParserRuleContext {
		public TerminalNode BEGIN() { return getToken(MPParser.BEGIN, 0); }
		public TerminalNode END() { return getToken(MPParser.END, 0); }
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitBody(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(BEGIN);
			setState(47);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(46);
				stmt();
				}
			}

			setState(49);
			match(END);
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

	public static class StmtContext extends ParserRuleContext {
		public FuncallContext funcall() {
			return getRuleContext(FuncallContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MPParser.SEMI, 0); }
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitStmt(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			funcall();
			setState(52);
			match(SEMI);
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

	public static class FuncallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MPParser.ID, 0); }
		public TerminalNode LB() { return getToken(MPParser.LB, 0); }
		public TerminalNode RB() { return getToken(MPParser.RB, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public FuncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterFuncall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitFuncall(this);
		}
	}

	public final FuncallContext funcall() throws RecognitionException {
		FuncallContext _localctx = new FuncallContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_funcall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(ID);
			setState(55);
			match(LB);
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INTLIT) {
				{
				setState(56);
				exp();
				}
			}

			setState(59);
			match(RB);
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

	public static class ExpContext extends ParserRuleContext {
		public TerminalNode INTLIT() { return getToken(MPParser.INTLIT, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(INTLIT);
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

	public static class MtypeContext extends ParserRuleContext {
		public TerminalNode INTTYPE() { return getToken(MPParser.INTTYPE, 0); }
		public MtypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mtype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).enterMtype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MPListener ) ((MPListener)listener).exitMtype(this);
		}
	}

	public final MtypeContext mtype() throws RecognitionException {
		MtypeContext _localctx = new MtypeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_mtype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(INTTYPE);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17D\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26"+
		"\n\2\r\2\16\2\27\3\2\3\2\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6\62\n\6\3\6\3\6\3\7"+
		"\3\7\3\7\3\b\3\b\3\b\5\b<\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\2\2\13\2\4\6"+
		"\b\n\f\16\20\22\2\2\2>\2\25\3\2\2\2\4\35\3\2\2\2\6\37\3\2\2\2\b&\3\2\2"+
		"\2\n/\3\2\2\2\f\65\3\2\2\2\168\3\2\2\2\20?\3\2\2\2\22A\3\2\2\2\24\26\5"+
		"\4\3\2\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3"+
		"\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\36\5\b\5\2\34\36\5\6\4\2\35\33\3"+
		"\2\2\2\35\34\3\2\2\2\36\5\3\2\2\2\37 \7\t\2\2 !\7\16\2\2!\"\7\4\2\2\""+
		"#\7\5\2\2#$\7\6\2\2$%\5\n\6\2%\7\3\2\2\2&\'\7\n\2\2\'(\7\16\2\2()\7\4"+
		"\2\2)*\7\5\2\2*+\7\7\2\2+,\5\22\n\2,-\7\6\2\2-.\5\n\6\2.\t\3\2\2\2/\61"+
		"\7\13\2\2\60\62\5\f\7\2\61\60\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\64"+
		"\7\f\2\2\64\13\3\2\2\2\65\66\5\16\b\2\66\67\7\6\2\2\67\r\3\2\2\289\7\16"+
		"\2\29;\7\4\2\2:<\5\20\t\2;:\3\2\2\2;<\3\2\2\2<=\3\2\2\2=>\7\5\2\2>\17"+
		"\3\2\2\2?@\7\3\2\2@\21\3\2\2\2AB\7\r\2\2B\23\3\2\2\2\6\27\35\61;";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}