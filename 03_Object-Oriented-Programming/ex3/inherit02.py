class M:
    def foo(self, i):
        print(i * 2)
        self.foo(i)

    def bar(self, i):
        print(i * 10)


class N(M):
    def bar(self, i):
        print(-i)
        super().bar(i)

class Q(N):
    def foo(self, i):
        print(i * i)
        super().bar(i)
        self.bar(i)
    
    def bar(self, i):
        print(i - 100)


x = Q()

N.foo(x, 3) 
# 6
# 9
# -3
# 30
# -97

# gọi foo của N, N ko foo, dùng cha là M, gọi foo của M.
# M foo -> self là x, kiểu Q, còn i = 3.
# dòng đầu ra 3 * 2 = 6
# dòng 2 self.foo -> x.foo -> foo ở Q (do override của N) -> print(3 * 3) = 9
# lúc Q gọi foo, có gọi super bar -> N gọi bar -> in -i, rồi gọi super bar -> lên M gọi bar
# sau đó Q self bar -> gọi bar của nó i-100