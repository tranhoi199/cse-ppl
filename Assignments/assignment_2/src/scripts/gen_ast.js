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
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, ${300+i}))
`
}

fs.writeFileSync(path.join(dist, './gen_ast.py'), text, 'utf8');