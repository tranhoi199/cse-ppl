const fs = require('fs');
const path = require('path');

let text = '';

for (let i = 1; i < 101; i++) {
        text += `
    def test_${i}(self):
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, ${200 + i}))
        
`
}

fs.writeFileSync(path.join(__dirname, './build/parser_script.py'), text, 'utf8');