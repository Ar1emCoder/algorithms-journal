class Solution:
    def isPalindrome(self, s: str) -> bool:
        stroka = ""
        for st in range(len(s)):
            if s[st].isalnum():
                stroka += s[st]
        stroka = stroka.strip().lower()

        left, right = 0, len(stroka) - 1
        while left <= right:
            if stroka[left] == stroka[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# Time Complexity: O(N) - один проход для очистки, один проход для проверки
# Space Complexity: O(N) - для создания очищенной строки
