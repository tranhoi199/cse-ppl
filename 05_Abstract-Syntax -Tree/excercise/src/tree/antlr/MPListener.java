// Generated from MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MPParser}.
 */
public interface MPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MPParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MPParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(MPParser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(MPParser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#procdecl}.
	 * @param ctx the parse tree
	 */
	void enterProcdecl(MPParser.ProcdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#procdecl}.
	 * @param ctx the parse tree
	 */
	void exitProcdecl(MPParser.ProcdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#funcdecl}.
	 * @param ctx the parse tree
	 */
	void enterFuncdecl(MPParser.FuncdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#funcdecl}.
	 * @param ctx the parse tree
	 */
	void exitFuncdecl(MPParser.FuncdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(MPParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(MPParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(MPParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(MPParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#funcall}.
	 * @param ctx the parse tree
	 */
	void enterFuncall(MPParser.FuncallContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#funcall}.
	 * @param ctx the parse tree
	 */
	void exitFuncall(MPParser.FuncallContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(MPParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(MPParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#mtype}.
	 * @param ctx the parse tree
	 */
	void enterMtype(MPParser.MtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#mtype}.
	 * @param ctx the parse tree
	 */
	void exitMtype(MPParser.MtypeContext ctx);
}