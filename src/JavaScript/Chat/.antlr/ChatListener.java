// Generated from f:/Food-Recipe-Chatbot/src/Python/Chat/Chat.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ChatParser}.
 */
public interface ChatListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ChatParser#chat}.
	 * @param ctx the parse tree
	 */
	void enterChat(ChatParser.ChatContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatParser#chat}.
	 * @param ctx the parse tree
	 */
	void exitChat(ChatParser.ChatContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(ChatParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(ChatParser.LineContext ctx);
}