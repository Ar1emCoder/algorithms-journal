class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water


# Time Complexity: O(N) — каждый элемент обрабатывается ровно один раз (левый или правый указатель двигается на каждой итерации)
# Space Complexity: O(1) — используем только 4 переменные (left, right, left_max, right_max, water)
