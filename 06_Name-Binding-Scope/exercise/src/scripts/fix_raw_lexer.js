const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = fs.readFileSync(path.join(__dirname, '../test/LexerSuite.py'));

text = String(text)
    .replace(/.test\([\r\n]([^"r])*"""/g, `.test(
            r"""`
);

fs.writeFileSync(path.join(dist, './fix_raw_lexer.py'), text, 'utf8');