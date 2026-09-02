from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def bfs(grid, r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])) or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            bfs(grid, r, c+ 1)
            bfs(grid, r, c - 1)
            bfs(grid, r + 1, c)
            bfs(grid, r - 1, c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    bfs(grid, i, j)
        return cnt


# Time Complexity: O(M * N) — посещаем каждую клетку максимум 1 раз
# Space Complexity: O(M * N) — глубина стека рекурсии в худшем случае (вся сетка — остров)