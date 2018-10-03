const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = fs.readFileSync(path.join(__dirname, '../test/LexerSuite.py'));

text = String(text).replace(/test_.*\(/g, (num) => {
    return 'test_' + crypto.randomBytes(15).toString('hex') + '(';
}).replace(/""" Test.*"""/g, '""" Test ... """')

fs.writeFileSync(path.join(dist, './LexerSuite.py'), text, 'utf8');