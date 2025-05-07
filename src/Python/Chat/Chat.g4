grammar Chat;

chat: (line)+ ;

line: NAME ':' MESSAGE;

NAME: [a-zA-Z]+;  // Matches words like Alice, Bob, etc.

MESSAGE: ~[:\n]+ ;  // Matches the message text after the colon, excluding the colon and newline

WS: [ \t\n\r]+ -> skip;  // Skips whitespaces and newlines
