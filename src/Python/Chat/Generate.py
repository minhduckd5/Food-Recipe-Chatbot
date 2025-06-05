import subprocess
import os

# Define paths
antlr_jar = os.path.abspath("libs/antlr-4.13.2-complete.jar")
grammar_file = "Chat.g4"
output_dir = "CompiledFile"

# Make sure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Build the ANTLR command
command = [
    "java", "-jar", antlr_jar,
    "-Dlanguage=Python3",
    "-o", output_dir,
    grammar_file
]

# Run the command
try:
    subprocess.run(command, check=True)
    print(f"ANTLR generation successful. Files saved to '{output_dir}'")
except subprocess.CalledProcessError as e:
    print(f"Error running ANTLR: {e}")