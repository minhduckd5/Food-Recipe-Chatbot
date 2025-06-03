import antlr4 from 'antlr4';
import fs from 'fs';
import path from 'path';

import ChatLexer from '../../../CompiledFile/ChatLexer.js';
import ChatParser from '../../../CompiledFile/ChatParser.js';

const inputText = `john SHOUTS: hello @michael /pink/this will work/ :-) \n`;

const inputStream = new antlr4.InputStream(inputText);
const lexer = new ChatLexer(inputStream);
const tokenStream = new antlr4.CommonTokenStream(lexer);
const parser = new ChatParser(tokenStream);

// Set the entry point based on your grammar
const tree = parser.chat(); // 'chat' should be the rule name

// Convert the parse tree to string (like Python's toStringTree)
const result = tree.toStringTree(parser.ruleNames);

// Ensure output folder exists
const outputFolder = 'CompiledFile';
const outputFile = path.join(outputFolder, 'output.txt');

if (!fs.existsSync(outputFolder)) {
    fs.mkdirSync(outputFolder, { recursive: true });
}

fs.writeFileSync(outputFile, result, 'utf8');

console.log(`Parsing complete. Output written to ${outputFile}`);
