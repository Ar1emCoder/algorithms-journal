class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# Time Complexity: O(amount * len(coins)) - для каждой суммы от 1 до amount перебираем все монеты.
# Space Complexity: O(amount) - массив dp размером amount + 1.
