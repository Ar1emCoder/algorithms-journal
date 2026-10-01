class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left, max_len = 0, 0

        for right in range(len(s)):
            ch = s[right]
            while ch in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(ch)
            max_len = max(max_len, right - left + 1)
        return max_len


# Time Complexity: O(N) - каждый символ обрабатывается максимум 2 раза
# Space Complexity: O(min(N, M)) - где M размер алфавита
