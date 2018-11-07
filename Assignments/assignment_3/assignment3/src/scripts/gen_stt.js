const fs = require('fs');
const path = require('path');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = '';

for (let i = 151; i <= 170; i++) {
    text += `
    def test_${i}(self):
        input = r"""

procedure main();
begin

end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, ${100 + i}))

`
}

fs.writeFileSync(path.join(dist, './gen_stt.py'), text, 'utf8');