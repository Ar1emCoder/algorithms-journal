class Solution:
    def minTimeToType(self, word: str) -> int:
        timer = 0
        curr = "a"

        for char in word:
            distance = abs(ord(char) - ord(curr))
            other_distance = 26 - distance
            move_time = min(distance, other_distance)
            timer += 1 + move_time
            curr = char

        return timer


# Time Complexity: O(N)
# Space Complexity: O(1)
