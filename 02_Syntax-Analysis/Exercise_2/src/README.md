```bash
# run python
sudo pip3 install antlr4-python3-runtime
python3 run.py gen

python3 run.py test LexerSuite
python3 run.py test ParserSuite

# draw parse tree
antlr4 MP.g4                
javac *.java                
grun MP program -f code.txt -gui
```