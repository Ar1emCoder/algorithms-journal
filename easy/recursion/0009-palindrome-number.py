class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revers_x = 0
        while x > revers_x:
            revers_x = revers_x * 10 + x % 10
            x //= 10
        return x == revers_x or x == revers_x // 10


# Time Complexity: O(log n) - количество цифр в числе
# Space Complexity: O(1) - используем только переменную revers_x
