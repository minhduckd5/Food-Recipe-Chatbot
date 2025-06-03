import ChatListener from '../../../CompiledFile/ChatListener.js';
import ChatParser from '../../../CompiledFile/ChatParser.js';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

export default class HtmlChatListener extends ChatListener {
    constructor(res) {
        super();
        this.Res = res;
    }

    enterName(ctx) {
        this.Res.write("<strong>");
    }

    exitName(ctx) {
        this.Res.write(ctx.WORD().getText());
        this.Res.write("</strong> ");
    }

    exitEmoticon(ctx) {
        const emoticon = ctx.getText();
        if (emoticon === ':-)' || emoticon === ':)') {
            this.Res.write("🙂");
        } else if (emoticon === ':-(' || emoticon === ':(') {
            this.Res.write("🙁");
        } else {
            this.Res.write(emoticon);
        }
    }

    enterCommand(ctx) {
        if (ctx.SAYS() != null)
            this.Res.write(ctx.SAYS().getText() + ':' + '<p>');

        if (ctx.SHOUTS() != null)
            this.Res.write(ctx.SHOUTS().getText() + ':' + '<p style="text-transform: uppercase">');
    }

    exitLine(ctx) {
        this.Res.write("</p>");
    }

    enterColor(ctx) {
        const color = ctx.WORD().getText();
        this.Res.write('<span style="color: ' + color + '">');
    }

    exitColor(ctx) {
        ctx.text += ctx.message().text;
        ctx.text += '</span>';
    }


    exitMessage(ctx) {
        const __filename = fileURLToPath(import.meta.url);
        const __dirname = dirname(__filename);

        let text = '';
        console.log(ctx.children[0]);
        

        for (let index = 0; index < ctx.children.length; index++) {
            if (ctx.children[index].text != null)
                text += ctx.children[index].text;
            else
                text += ctx.children[index].getText();
        }

        if (!(ctx.parentCtx instanceof ChatParser.LineContext)) {
            ctx.text = text;
        } else {
            this.Res.write(text);
            this.Res.write("</p>");
        }

        const outputPath = path.join(__dirname, 'output.txt');
        fs.writeFileSync(outputPath, text, { encoding: 'utf8' });
        console.log(`Text written to ${outputPath}`);
    }
}