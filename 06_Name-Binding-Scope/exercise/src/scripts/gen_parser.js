const fs = require('fs');
const path = require('path');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = '';

for (let i = 152; i < 180; i++) {
        text += `
    def test_${i}(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, ${200 + i}))
        
`
}

fs.writeFileSync(path.join(dist, './gen_parser.py'), text, 'utf8');