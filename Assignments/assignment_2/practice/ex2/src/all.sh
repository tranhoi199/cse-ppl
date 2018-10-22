echo "Cleaning and Generatting..."
python3 "./run.py" clean
python3 "./run.py" gen

echo "Generate successfully"


echo "Testing AST..."
python3 "./run.py" test ASTGenSuite