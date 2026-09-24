class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # while k > 0:
        #     last = nums.pop()
        #     nums.insert(0, last)
        #     k -= 1
        k = k % len(nums)

        def reverse(left, right):
            while left < right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)


# Time Complexity: O(n) - три линейных прохода (реверса)
# Space Complexity: O(1) - модифицируем массив in-place
