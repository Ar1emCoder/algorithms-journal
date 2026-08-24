class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)


# Time Complexity: O(log n) — делим n пополам на каждом шаге
# Space Complexity: O(log n) — глубина стека вызовов
