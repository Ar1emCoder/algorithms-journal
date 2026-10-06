class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]


# Time Complexity: O(m * n) - где m количество строк, n количество столбцов.Проходим по всей сетке один раз.
# Space Complexity: O(1) - модифицируем входной массив grid на месте,не создаём дополнительных структур данных.
