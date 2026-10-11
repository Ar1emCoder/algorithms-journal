class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]  # or dp[-1][-1]


# Time Complexity: O(m * n) - где m и n длины строк text1 и text2. Заполняем таблицу dp размером (m+1) x (n+1).
# Space Complexity: O(m * n) - создаём двумерный массив dp. (Можно оптимизировать до O(min(m, n)), храня только  две строки, но полная таблица нагляднее для понимания.)