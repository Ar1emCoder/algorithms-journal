class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# Time Complexity: O(2^n) — экспоненциальная, т.к. каждый вызов создает два новых
# Space Complexity: O(n) — глубина стека вызовов
