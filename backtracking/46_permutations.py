from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur_subset):
            if len(cur_subset) == len(nums):
                res.append(cur_subset[:])
                return

            for i in range(len(nums)):
                if nums[i] in cur_subset:
                    continue

                cur_subset.append(nums[i])
                backtrack(cur_subset)
                cur_subset.pop()
        backtrack([])
        return res


# Time Complexity: O(n * n!) — n! перестановок, каждая копируется за O(n)
# Space Complexity: O(n) — глубина стека рекурсии