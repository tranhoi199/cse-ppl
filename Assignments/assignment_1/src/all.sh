echo "Cleaning and Generatting..."
python3 run.py clean
python3 run.py gen

echo "Testing Lexer..."
python3 run.py test LexerSuite

echo "Testing Parser..."
python3 run.py test ParserSuite