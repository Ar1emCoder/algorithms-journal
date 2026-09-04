from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        cnt = 0

        def dfs(city):
            if city in isConnected:
                return
            visited.add(city)

            for j in range(n):
                if isConnected[city][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                cnt += 1
                dfs(i)
        return cnt


# Time Complexity: O(M * N)
# Space Complexity: O(M * N)
