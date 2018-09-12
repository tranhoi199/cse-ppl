const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = '';

for (let i = 72; i < 101; i++) {
    let name = 'd' + crypto.randomBytes(5).toString('hex');
    let func = 'e' + crypto.randomBytes(5).toString('hex');
    let arg1 = 'g' + crypto.randomBytes(5).toString('hex');
    let arg2 = 'p' + crypto.randomBytes(5).toString('hex');
    text += `
    def test_${i}(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure ${name}();
begin
    ${func}(${arg1}, ${arg2}) ;
end
""",

            r"procedure,${name},(,),;,begin,${func},(,${arg1},,,${arg2},),;,end,<EOF>",
            ${100+i}
        ))

`
}

fs.writeFileSync(path.join(dist, './fake_lexer.py'), text, 'utf8');