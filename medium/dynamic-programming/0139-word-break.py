class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j] == True:
                    dp[i] = True
                    break

        return dp[len(s)]


# Time Complexity: O(n³) - где n длина строки s. Два вложенных цикла O(n²), и на каждой итерации срез строки s[j:i] + проверка in wordDict занимают O(n) в худшем случае.
# Space Complexity: O(n) - массив dp размером n + 1.