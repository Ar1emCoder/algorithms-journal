from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(start, cur_subset):
            res.append(cur_subset[:])

            for i in range(start, len(nums)):
                cur_subset.append(nums[i])
                backtracking(i + 1, cur_subset)
                cur_subset.pop()

        backtracking(0, [])
        return res


# Time Complexity: O(n * 2^n) — 2^n подмножеств, каждое копируется за O(n)
# Space Complexity: O(n) — глубина стека рекурсии