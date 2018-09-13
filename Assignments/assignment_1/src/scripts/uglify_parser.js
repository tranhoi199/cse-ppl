const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = fs.readFileSync(path.join(__dirname, '../test/ParserSuite.py'));

text = String(text).replace(/test_.*\(/g, (num) => {
    return 'test_' + crypto.randomBytes(15).toString('hex') + '(';
})
.replace(/input = /g, '_1=')
.replace(/expect = /g, '_2=')
.replace(/""" Test.*"""/g, '""" Test ... """')
.replace(/.test\(input, expect, /g, '.test(_1,_2,')

fs.writeFileSync(path.join(dist, './ParserSuite.py'), text, 'utf8');