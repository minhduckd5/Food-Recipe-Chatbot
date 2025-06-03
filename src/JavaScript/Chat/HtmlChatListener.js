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
            ctx.text = "🙂";
        } else if (emoticon === ':-(' || emoticon === ':(') {
            ctx.text = "🙁";
        } else {
            ctx.text = emoticon; // fallback
        }
    }

    enterCommand(ctx) {
        if (ctx.SAYS()) {
            this.Res.write(ctx.SAYS().getText() + ': <p>');
        } else if (ctx.SHOUTS()) {
            this.Res.write(ctx.SHOUTS().getText() + ': <p style="text-transform: uppercase">');
        }
    }

    exitLine(ctx) {
        this.Res.write("</p>");
    }

    enterColor(ctx) {
        const color = ctx.WORD().getText();
        this.Res.write('<span style="color: ' + color + '">');
    }

    exitColor(ctx) {
        const color = ctx.WORD().getText();
        this.Res.write('<span style="color: ' + color + '">');
        this.Res.write(ctx.message().text);
        this.Res.write('</span>');
    }


    exitMessage(ctx) {
        let text = '';
        for (let child of ctx.children) {
            if (child.text != null) {
                text += child.text;
            } else {
                text += child.getText();
            }
        }

        if (!(ctx.parentCtx instanceof ChatParser.LineContext)) {
            ctx.text = text;
        } else {
            this.Res.write(text);
            this.Res.write("</p>");
        }
    }
}