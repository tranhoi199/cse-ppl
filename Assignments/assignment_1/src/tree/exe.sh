alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar" org.antlr.v4.Tool'

alias grun='java org.antlr.v4.gui.TestRig'

export ANTLR_LIB="/usr/local/lib/antlr-4.7.1-complete.jar"




antlr4 MP.g4 -o antlr


javac ./antlr/*.java -d ./


grun MP program -f ./test/$1.txt -gui