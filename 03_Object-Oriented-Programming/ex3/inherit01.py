class M:
    def foo(self, i):
        print(i * 2)
        self.foo(i)

class N(M):
    pass

class Q(N):
    def foo(self, i):
        print(i * i)


x = Q()

N.foo(x, 3) 
# 6
# 9

# gọi foo của N, N ko foo, dùng cha là M, gọi foo của M.
# M foo -> self là x, kiểu Q, còn i = 3.
# dòng đầu ra 3 * 2 = 6
# dòng 2 self.foo -> x.foo -> foo ở Q (do override của N) -> print(3 * 3) = 9