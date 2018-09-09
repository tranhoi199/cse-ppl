const fs = require('fs');
const path = require('path');

let text = '';

for (let i = 1; i < 101; i++) {
    text += `
    def test_${i}(self):
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            ${100 + i}
        ))
        
`
}

fs.writeFileSync(path.join(__dirname, './build/lexer_script.py'), text, 'utf8');