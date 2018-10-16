class O: pass

class A(O): pass
class B(O): pass
class C(O): pass

class D(A,B): pass
class E(B,C): pass

class F(D,E,C): pass

print(F.mro())