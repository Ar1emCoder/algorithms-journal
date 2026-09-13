from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_summa = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_summa = nums[i] + nums[left] + nums[right]

                if abs(curr_summa - target) < abs(best_summa - target):
                    best_summa = curr_summa

                if curr_summa < target:
                    left += 1
                else:
                    right -= 1
        return best_summa


# Time Complexity: O(n²) — сортировка O(n log n) + внешний цикл O(n) * two pointers O(n)
# Space Complexity: O(1) или O(n) в зависимости от реализации сортировки
