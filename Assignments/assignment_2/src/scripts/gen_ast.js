const fs = require('fs');
const path = require('path');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = '';

for (let i = 120; i <= 135; i++) {
    text += `
    def test_${i}(self):
        input = r"""

"""
        expect = str()
        self.assertTrue(TestAST.test(input, expect, ${300+i}))
`
}

fs.writeFileSync(path.join(dist, './gen_ast.py'), text, 'utf8');