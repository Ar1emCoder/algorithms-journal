from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited) -> bool:
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor, visited):
                    return True
            return False

        return dfs(source, set())


# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
