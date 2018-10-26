const fs = require('fs');
const path = require('path');

const filepath = path.join(__dirname, '../test/ASTGenSuite.py')

fs.copyFileSync(filepath, path.join(__dirname, '../test/', `ASTGenSuite_${new Date().getTime()}.py`))

let text = fs.readFileSync(filepath);

text = String(text)
.replace(/(expect\s*=\s*)(r?"""|r?'''|r?["']|str\()([^\r\n]*)("""|'''|["']|\))(\s*[\r\n]\s*self.assertTrue\(\s*TestAST.test\(\s*input\s*,\s*expect\s*,\s*)(\d+)(\s*\)\))/g,
    (match, p1, p2, p3, p4, p5, p6, p7) => {
        let numFile = p6;
        console.log('Replacing file ' + numFile);

        solFilePath = path.join(__dirname, '../test/solutions/', numFile + '.txt')

        if (!fs.existsSync(solFilePath)) {
            console.log('File ' + numFile + 'isnt exist')
            fs.writeFileSync(solFilePath, 'Program([])')
            console.log('Created file ' + numFile);
        }

        let solution = fs.readFileSync(solFilePath)
        console.log('File ' + numFile + ' OK');

        return p1 + 'str(' + solution + ')' + p5 + p6 + p7
    })


fs.writeFileSync(path.join(__dirname, '../test/ASTGenSuite.py'), text, 'utf8');
