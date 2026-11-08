from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        cnt = 0

        def dfs(city):
            if city in visited:
                return
            visited.add(city)

            for j in range(len(isConnected)):
                if isConnected[city][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(len(isConnected)):
            if i not in visited:
                cnt += 1
                dfs(i)

        return cnt


# Time Complexity: O(N^2)
# Space Complexity: O(N)
