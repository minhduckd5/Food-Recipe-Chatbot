import os
import sys
import os
from antlr4 import *

# Add the CompiledFile directory to the system path
sys.path.append(os.path.join(os.getcwd(), "CompiledFile"))

from ChatLexer import ChatLexer
from ChatParser import ChatParser
import sys

def main():
    # Example input (you can replace this with file input)
    input_text = """
    Alice: Hello!
    Bob: Hi there!
    """

    # Convert input text to a stream for the lexer
    input_stream = InputStream(input_text)

    # Lexing and parsing
    lexer = ChatLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ChatParser(token_stream)

    # Parse the input (entry point rule is 'chat' in Chat.g4)
    tree = parser.chat()

    # Convert parse tree to string
    result = tree.toStringTree(recog=parser)

    # Create the 'CompiledFile' folder if it doesn't exist
    output_folder = "CompiledFile"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write the result to a file inside the 'CompiledFile' folder
    output_file = os.path.join(output_folder, "output.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Parsing complete. Output written to {output_file}")

if __name__ == '__main__':
    main()
