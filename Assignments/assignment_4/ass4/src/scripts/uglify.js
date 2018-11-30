const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = fs.readFileSync(path.join(__dirname, '../test/CodeGenSuite_ALL.py'));

text = String(text).replace(/def test.*\(/g, () => {
    return 'def test_' + crypto.randomBytes(10).toString('hex') + '(';
})

let numfile = 100;

text = String(text).replace(/TestCodeGen.test\(input\s*,\s*expect\s*,\s*.*\)\)/g, () => {
    return 'TestCodeGen.test(input, expect, ' + ++numfile + '))';
})

fs.writeFileSync(path.join(__dirname, '../test/CodeGenSuite_MIN.py'), text, 'utf8');