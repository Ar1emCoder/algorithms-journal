from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = [0]

        while stack:
            curr_room = stack.pop()
            for key in rooms[curr_room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        return len(visited) == len(rooms)


# Time Complexity: O(N + M) where N = rooms, M = total keys
# Space Complexity: O(N) for visited set and stack
