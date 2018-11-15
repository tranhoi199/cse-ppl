const fs = require('fs');
const path = require('path');

const dist = path.join(__dirname, './dist');

if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist)
}

let text = '';

for (let i = 1; i <= 100; i++) {
    text += `
    def test_${i}(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, ${100 + i}))

`
}

fs.writeFileSync(path.join(dist, './gen.py'), text, 'utf8');