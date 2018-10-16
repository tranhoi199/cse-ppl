const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = '';

function fakeAZ() {
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    return possible.charAt(Math.floor(Math.random() * possible.length));
}

function fakeValid() {
    let txt = `function procedure begin end true false if then else for while with do to downto return break continue integer string real boolean array var of and then or else div mod not and or + - * / := <= >= <> = < > ( ) [ ] ; , : , .. + - * / := <= >= <> = < > ( ) [ ] ; , : , ..`
    const possible = txt.split('\n').join(' ').split(' ');
    return possible[(Math.floor(Math.random() * possible.length))];
}

const fake = () => fakeAZ() + crypto.randomBytes(2).toString('hex');

for (let i = 72; i < 101; i++) {
    let gen = fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fake() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid()+ ' '
        + fake() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' '
        + fakeValid() + ' ' + fakeValid() + ' ' + fake() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid() + ' ' + fakeValid();
    text += `
    def test_${i}_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
// ${fakeValid()},${fakeValid()},${fakeValid()} ${fake()} ${fakeValid()} ${fakeValid()},${fakeValid()},${fakeValid()}
${gen}
(* ${fakeValid()} ${fakeValid()} ${fake()},${fakeValid()},${fake()} ${fakeValid()} ${fake()},${fakeValid()},${fakeValid()}*)
""",

            r"${gen.split(' ').join(',')},<EOF>",
            ${100 + i}
        ))

`
}

fs.writeFileSync(path.join(dist, './fake_lexer.py'), text, 'utf8');