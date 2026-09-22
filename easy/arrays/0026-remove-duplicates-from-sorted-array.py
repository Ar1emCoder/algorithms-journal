class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        uniq_indx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[uniq_indx]:
                uniq_indx += 1
                nums[uniq_indx] = nums[i]
        return uniq_indx + 1


# Time Complexity: O(n) - один проход по массиву
# Space Complexity: O(1) - модифицируем in-place
