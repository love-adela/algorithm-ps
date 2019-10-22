class Solution:
    def multiply_matrix(self, a, b):
        return (
                a[0]*b[0] + a[1]*b[2],
                a[0]*b[1] + a[1]*b[3],
                a[2]*b[0] + a[3]*b[2],
                a[2]*b[1] + a[3]*b[3]
                )


    def fibo_matrix(self, n):
        if n == 0:
            return (1, 0, 0, 1)
        if n == 1:
            return (1, 1, 1, 0)

        a = self.fibo_matrix(n//2)
        a_square = self.multiply_matrix(a,a)
        if n % 2 == 0:
            return a_square
        else:
            return self.multiply_matrix(a_square, (1, 1, 1, 0))


    def fib(self, N:int)->int:
        if N == 0:
            return 0
        return self.fibo_matrix(N-1)[0]


def test_solution():
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
