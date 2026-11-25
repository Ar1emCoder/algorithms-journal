from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Finds the length of the longest subarray with maximum bitwise AND.
        Since bitwise AND of a subarray <= its max element, we just need
        the longest contiguous streak of the maximum element.
        """
        max_value = max(nums)
        curr_len, max_len = 0, 0

        for num in nums:
            if num == max_value:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            else:
                curr_len = 0

        return max_len


# Time Complexity: O(N)
# Space Complexity: O(1)
