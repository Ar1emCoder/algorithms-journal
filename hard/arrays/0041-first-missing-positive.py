from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        zn = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                if zn == nums[i]:
                    zn += 1
        return zn


# Time Complexity: O(N log N) - из-за сортировки (оптимальное решение требует O(N))
# Space Complexity: O(1) или O(N) в зависимости от реализации сортировки в Python
