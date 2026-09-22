class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0

        uniq_indx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[uniq_indx] = nums[i]
                uniq_indx += 1
        return uniq_indx


# Time Complexity: O(n) - один проход по массиву
# Space Complexity: O(1) - модифицируем in-place
