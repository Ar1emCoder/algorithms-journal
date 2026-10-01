class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        curr_sum, min_len = 0, float("inf")

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        if min_len != float("inf"):
            return min_len
        else:
            return 0


# Time Complexity: O(N) - каждый элемент обрабатывается максимум 2 раза
# Space Complexity: O(1) - используем только переменные
