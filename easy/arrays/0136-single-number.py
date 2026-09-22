class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


# Time Complexity: O(n) - один проход по массиву
# Space Complexity: O(1) - используем только одну переменную result
