;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Tue Nov 27 16:38:25 ICT 2018

.source HelloWorld.java
.class public HelloWorld
.super java/lang/Object


.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this LHelloWorld; from Label0 to Label1

Label0:
.line 3
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 2
.limit locals 1
.var 0 is arg0 [Ljava/lang/String; from Label0 to Label1

Label0:
.line 5
	getstatic java.lang.System.out Ljava/io/PrintStream;
	ldc "Hello World!"
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
Label1:
.line 6
	return

.end method
