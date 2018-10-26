const fs = require('fs');
const path = require('path');

const filepath = path.join(__dirname, '../test/ASTGenSuite.py')

let text = fs.readFileSync(filepath);

text = String(text)
.replace(/expect = str\((.*[\r\n]){1,2}.*\)/g, 'expect = r""')

fs.writeFileSync(path.join(__dirname, './dist/ast_str2raw.py'), text, 'utf8');
