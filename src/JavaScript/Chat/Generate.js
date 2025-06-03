import { execFile } from 'child_process';
import { mkdirSync, existsSync } from 'fs';
import path from 'path';

// Define paths
const antlrJar = path.resolve('src/JavaScript/Chat/libs/antlr-4.13.2-complete.jar');
const grammarFile = path.resolve('src/JavaScript/Chat/Chat.g4');
const outputDir = path.resolve('CompiledFile');

// Ensure output directory exists
if (!existsSync(outputDir)) {
    mkdirSync(outputDir, { recursive: true });
}

// Build the ANTLR command
const command = 'java';
const args = [
    '-jar', antlrJar,
    '-Dlanguage=JavaScript',
    '-o', outputDir,
    grammarFile
];

// Run the command
execFile(command, args, (error, stdout, stderr) => {
    if (error) {
        console.error(`Error running ANTLR: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`ANTLR stderr:\n${stderr}`);
    }
    console.log(`ANTLR generation successful. Files saved to '${outputDir}'`);
});
