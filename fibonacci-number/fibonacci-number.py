class Solution:
    def fib(self, n: int) -> int:
        
        check = {}
        if n < 0:
            return 0
        
        def yo(n):
            if n in check:
                return check[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            check[n] = yo(n-1) + yo(n-2)
            return check[n]
        
        return yo(n)