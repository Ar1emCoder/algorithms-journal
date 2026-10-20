class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid

        return left


# Time Complexity: O(log n) - на каждом шаге область поиска делится пополам.
# Space Complexity: O(1) - используем только константную память (left, right, mid).
