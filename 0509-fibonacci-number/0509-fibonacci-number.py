class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        while n >= 2:
            return self.fib(n-1) + self.fib(n - 2)