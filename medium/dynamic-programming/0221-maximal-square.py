class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        max_size = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        # Инициализируем первую строку и первый столбец
        for j in range(cols):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0
            max_size = max(max_size, dp[0][j])

        for i in range(rows):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            max_size = max(max_size, dp[i][0])

        # Заполняем таблицу: минимум из трёх соседей + 1
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    max_size = max(max_size, dp[i][j])

        # Площадь квадрата = сторона^2
        return max_size * max_size

    
# Time Complexity: O(m * n) - где m и n размеры матрицы. Один проход по всем ячейкам.
# Space Complexity: O(m * n) - создаём таблицу dp того же размера. (Можно оптимизировать до O(n), храня только предыдущую строку.)