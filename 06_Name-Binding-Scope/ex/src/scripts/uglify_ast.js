const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = fs.readFileSync(path.join(__dirname, '../test/ASTGenSuite.py'));

text = String(text).replace(/test_.*\(/g, (num) => {
    return 'test_' + crypto.randomBytes(10).toString('hex') + '(';
})

fs.writeFileSync(path.join(dist, './ASTGenSuite.py'), text, 'utf8');