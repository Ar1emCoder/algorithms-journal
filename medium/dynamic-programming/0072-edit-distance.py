class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Базовые случаи: преобразование в/из пустой строки
        for j in range(n + 1):
            dp[0][j] = j  # вставка j символов
        for i in range(m + 1):
            dp[i][0] = i  # удаление i символов

        # Заполняем таблицу
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]  # символы совпадают, операция не нужна
                else:
                    # 1 + min(удаление, вставка, замена)
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[m][n]


# Time Complexity: O(m * n) - где m и n длины строк. Заполняем таблицу dp.
# Space Complexity: O(m * n) - создаём таблицу dp размером (m+1) x (n+1). (Можно оптимизировать до O(min(m, n)), храня только две строки.)