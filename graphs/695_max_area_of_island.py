from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0

            return (
                1
                + dfs(grid, r, c + 1)
                + dfs(grid, r, c - 1)
                + dfs(grid, r + 1, c)
                + dfs(grid, r - 1, c)
            )

        max_S = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_S = dfs(grid, i, j)
                    if max_S < curr_S:
                        max_S = curr_S
        return max_S


# Time Complexity: O(M * N), где M - количество строк, N - количество столбцов.
# Space Complexity: O(M * N) в худшем случае. Это глубина стека рекурсии, если вся сетка будет состоять из '1' (один огромный остров).
