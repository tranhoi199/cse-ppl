const fs = require('fs');
const path = require('path');

const filepath = path.join(__dirname, '../test/ASTGenSuite.py')

fs.copyFileSync(filepath, path.join(__dirname, '../test/~ASTGenSuite.py'))

let text = fs.readFileSync(filepath);

text = String(text)
.replace(/(IntType|FloatType|BoolType|StringType|Break|Continue)([^(])/g, (match, p1, p2) => p1 + '()' + p2)
.replace(/(Id|StringLiteral)(\()([^)'"]*)\)/g, (match, p1, p2, p3) => p1 + p2 + '"' + p3 + '")')
.replace(/(BinaryOp|UnaryOp)(\()([^,'"]*),/g,  (match, p1, p2, p3) => p1 + p2 + '"' + p3 + '",')
.replace(/Return\(Some\((\s\d)\)\)/)
// FuncDecl
// For

fs.writeFileSync(path.join(__dirname, './dist/ast_raw2str.py'), text, 'utf8');