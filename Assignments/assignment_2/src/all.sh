echo "Cleaning and Generatting..."
python3 "./run.py" clean
python3 "./run.py" gen

echo "Generate successfully"

# echo "Fixing Expect AST..."
# node "./scripts/fix_expect_ast.js"

# echo "Backup file is ~ASTGenSuite.py!"

echo "Testing AST..."
python3 "./run.py" test ASTGenSuite