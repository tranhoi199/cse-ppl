const fs = require('fs');
const path = require('path');

const filepath = path.join(__dirname, '../test/ASTGenSuite.py')
// const filepath = path.join(__dirname, './backup/ASTGenSuite.py')

fs.copyFileSync(filepath, path.join(__dirname, '../test/~ASTGenSuite.py'))

let text = fs.readFileSync(filepath);

text = String(text)
.replace(/Id\(([^)'"]*)\)/g, (match, p1) => "Id('" + p1 + "')")
.replace(/StringLiteral\(([^)'"]*)\)/g, (match, p1) => "StringLiteral('" + p1 + "')")

.replace(/BinaryOp\(([^,'"]*),/g, (match, p1) => "BinaryOp('" + p1 + "',")
.replace(/UnaryOp\(([^,'"]*),/g, (match, p1) => "UnaryOp('" + p1 + "',")

.replace(/IntType([^(])/g, (match, p1) => "IntType()" + p1)
.replace(/FloatType([^(])/g, (match, p1) => "FloatType()" + p1)
.replace(/BoolType([^(])/g, (match, p1) => "BoolType()" + p1)
.replace(/StringType([^(])/g, (match, p1) => "StringType()" + p1)

.replace(/Break([^(])/g, (match, p1) => "Break()" + p1)
.replace(/Continue([^(])/g, (match, p1) => "Continue()" + p1)


// fs.writeFileSync(path.join(__dirname, './dist/test.py'), text, 'utf8');
fs.writeFileSync(filepath, text, 'utf8');
