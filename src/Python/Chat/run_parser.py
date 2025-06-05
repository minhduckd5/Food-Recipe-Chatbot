import os
import sys
from antlr4 import *

# Add the CompiledFile directory to the system path
sys.path.append(os.path.join(os.getcwd(), "CompiledFile"))

from ChatLexer import ChatLexer
from ChatParser import ChatParser
from ChatListener import ChatListener
from ParseTreeWalker import ParseTreeWalker

def main():
    # Example inputs for testing the recipe chatbot
    test_inputs = [
        "search recipe for chicken curry",
        "show ingredients for vegetable stir fry",
        "how to make chicken curry",
        "suggest recipe with vegetables",
        "show recipe for vegetarian",
        "how long cooking time chicken curry",
        "substitute milk",
        "tip for chicken curry",
        "help",
        "hello"
    ]

    # Create the 'CompiledFile' folder if it doesn't exist
    output_folder = "CompiledFile"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each test input
    for i, input_text in enumerate(test_inputs, 1):
        print(f"\nProcessing test input {i}: {input_text}")
        
        # Convert input text to a stream for the lexer
        input_stream = InputStream(input_text)

        # Lexing and parsing
        lexer = ChatLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ChatParser(token_stream)

        # Parse the input
        tree = parser.chat()

        # Convert parse tree to string
        result = tree.toStringTree(recog=parser)

        # Write the result to a file
        output_file = os.path.join(output_folder, f"test_output_{i}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Input: {input_text}\n\n")
            f.write(f"Parse Tree:\n{result}")

        print(f"Output written to {output_file}")

if __name__ == '__main__':
    main()
