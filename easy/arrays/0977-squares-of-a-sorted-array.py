class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(result) - 1, -1, -1):
            if nums[left] ** 2 >= nums[right] ** 2:
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result


# Time Complexity: O(N) - один проход по массиву
# Space Complexity: O(1) - не считая массива результата, который не считается дополнительной памятью
