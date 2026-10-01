class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_v = 0

        while left < right:
            if max_v < (right - left) * min(height[left], height[right]):
                curr_val = (right - left) * min(height[left], height[right])
                max_v = max(max_v, curr_val)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_v


# Time:  O(N) — each element visited at most once
# Space: O(1) — only a few variables
