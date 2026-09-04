from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        def dfs(r, c):
            if (
                r < 0
                or r >= len(image)
                or c < 0
                or c >= len(image[0])
                or image[r][c] != orig_color
            ):
                return None
            image[r][c] = color

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        dfs(sr, sc)
        return image


# Time Complexity: O(M * N)
# Space Complexity: O(M * N)
