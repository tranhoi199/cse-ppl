const fs = require('fs');
const path = require('path');

const filepath = path.join(__dirname, '../test/ASTGenSuite.py')

let text = fs.readFileSync(filepath);

text = String(text)
.replace(/(expect\s*=\s*r?["'])([^\r\n]*)(["']\s*[\r\n]\s*self.assertTrue\(\s*TestAST.test\(\s*input\s*,\s*expect\s*,\s*)(\d+)(\)\))/g, (match, p1, p2, p3, p4, p5) => {
    let numFile = p4;
    console.log('File ' + numFile);
    let solution = fs.readFileSync(path.join(__dirname, '../test/solutions/', numFile + '.txt'))
    return p1 + solution + p3 + p4 + p5
})

fs.writeFileSync(path.join(__dirname, './dist/ast_sol2raw.py'), text, 'utf8');
