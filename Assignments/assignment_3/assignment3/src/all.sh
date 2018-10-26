echo "Cleaning..."
python3 "./run.py" clean
# python3 "./run.py" gen

# echo "Generate successfully"


echo "Testing Static Checker..."
python3 "./run.py" test CheckerSuite