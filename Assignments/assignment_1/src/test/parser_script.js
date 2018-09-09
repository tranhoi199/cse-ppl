const fs = require('fs');
const path = require('path');

let text = '';

for (let i = 41; i < 101; i++) {
        text += `
    def test_${i}(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, ${200 + i}))
        
`
}

fs.writeFileSync(path.join(__dirname, './build/parser_script.py'), text, 'utf8');