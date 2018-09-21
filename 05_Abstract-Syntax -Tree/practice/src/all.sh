echo "Cleaning and Generatting..."
python3 run.py clean
python3 run.py gen

echo "Testing AST..."
python3 run.py test ASTGenSuite