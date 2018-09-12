const fs = require('fs');
const path = require('path');

let text = fs.readFileSync(path.join(__dirname, '../main/mp/parser/MP.g4'));

text = String(text)
    .replace(/@lexer::.*\{[\r\n]*.*[\r\n]*\}/g, '')
    .replace(/Python3/g, 'Java')
    .replace(/(\w+\s*:[\s\w'"()\[\]\\|.?*+]+)(\{[\s\w'"()|.?*+-/=:\[\]]*\})([\s]*[;])/g, (match, p1, p2, p3) => {
        // console.log('\n========== Deteced Python Code: ============');
        // console.log(match);
        // console.log('--------------------------------------------');
        // console.log('\nPython Code:');
        // console.log(p2);
        return p1 + p3;
    })

fs.writeFileSync(path.join(__dirname, '../tree/MP.g4'), text, 'utf8');