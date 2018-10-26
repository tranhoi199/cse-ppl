const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = fs.readFileSync(path.join(__dirname, './backup/ASTGenSuite.py'));

text = String(text)
.replace(/input = """/g, 'input = r"""')
.replace(/expect = """/g, 'expect = r"""')
.replace(/expect = "/g, 'expect = r"')
.replace(/expect = '''/g, "expect = r'''");

fs.writeFileSync(path.join(dist, './fix_raw_ast.py'), text, 'utf8');