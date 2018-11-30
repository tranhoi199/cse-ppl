;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Fri Nov 30 07:21:34 ICT 2018

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
.limit stack 1
.limit locals 2
.var 0 is arg0 [Ljava/lang/String; from Label0 to Label1

Label0:
.line 6
	bipush 10
	anewarray java/lang/String
	astore_1
Label1:
.line 7
	return

.end method
