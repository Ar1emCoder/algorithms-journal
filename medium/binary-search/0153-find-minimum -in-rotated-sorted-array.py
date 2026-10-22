class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# Time Complexity: O(log n) - на каждом шаге область поиска делится пополам.
# Space Complexity: O(1) - используем только константную память (left, right, mid).
