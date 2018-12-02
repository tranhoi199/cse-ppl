;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Sun Dec 02 08:43:23 ICT 2018

.source a.java
.class public a
.super java/lang/Object


.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this La; from Label0 to Label1

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
	invokestatic a/foo()I
	invokevirtual java/io/PrintStream/println(I)V
Label1:
.line 6
	return

.end method

.method public static foo()I
.limit stack 2
.limit locals 1

.line 9
	iconst_5
	istore_0
.line 10
	iload_0
	iconst_2
	if_icmple Label0
Label3:
.line 11
	iload_0
	ifle Label1
.line 12
	iconst_5
	istore_0
.line 13
	iload_0
	iconst_5
	if_icmple Label2
	bipush 6
	ireturn
Label2:
	iconst_5
	istore_0
	goto Label3
Label1:
.line 15
	bipush 7
	istore_0
Label0:
.line 17
	iconst_4
	ireturn

.end method
