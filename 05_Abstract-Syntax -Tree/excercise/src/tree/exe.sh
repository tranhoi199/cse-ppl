echo "Converting ANTLR target from Python to Java"

node "../scripts/py2java.js"


echo "Searching ANTLR files"

alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar" org.antlr.v4.Tool'

alias grun='java org.antlr.v4.gui.TestRig'

export ANTLR_LIB="/usr/local/lib/antlr-4.7.1-complete.jar"

export CLASSPATH=".:/usr/local/lib/antlr-4.2.2-complete.jar:$CLASSPATH"


echo "Generating ANTLR to Java Code"

antlr4 MP.g4 -o antlr


echo "Generating Java Class files"

javac ./antlr/*.java -d ./


echo "Drawing Parse Tree"

grun MP program -f ./test/$1.txt -gui