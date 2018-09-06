alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar"'
antlr4 ./tc/MP.g4   
javac ./tc/*.java                
grun ./tc/MP program -f ./tc/code.txt -gui