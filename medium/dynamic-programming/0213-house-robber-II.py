class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: list[int]) -> int:
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]

            prev2 = houses[0]
            prev1 = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                curr = max(houses[i] + prev2, prev1)
                prev2, prev1 = prev1, curr

            return prev1

        # Два случая из-за круга:
        # 1) Не грабить последний дом (берём [0, n-2])
        # 2) Не грабить первый дом (берём [1, n-1])
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Time Complexity: O(N) - делаем два прохода по массиву (для двух случаев).
# Space Complexity: O(N) - использует срезы, создавая копии массива.
