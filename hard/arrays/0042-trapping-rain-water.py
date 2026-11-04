class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
                right -= 1

        return water


# Time Complexity: O(N) — каждый элемент обрабатывается ровно один раз (левый или правый указатель двигается на каждой итерации)
# Space Complexity: O(1)
