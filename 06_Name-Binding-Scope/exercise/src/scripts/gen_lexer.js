const fs = require('fs');
const path = require('path');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = '';

for (let i = 1; i < 101; i++) {
    text += `
    def test_${i}(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            ${100 + i}
        ))
        
`
}

fs.writeFileSync(path.join(dist, './gen_lexer.py'), text, 'utf8');