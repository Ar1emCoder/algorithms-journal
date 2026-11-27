from bisect import bisect_left


class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        # Оптимизированное решение через bisect: Time limit: O(n * log n)
        potions = sorted(potions)
        m = len(potions)
        result = []

        for spell in spells:
            target = success / spell
            first_complete = bisect_left(potions, target)
            result.append(m - first_complete)

        return result

        # НАИВНОЕ РЕШЕНИЕ: Time limit: O(n * m)
        # n, m = len(spells), len(potions)
        # pairs = [0] * n

        # for i in range(n):
        #     for j in range(m):
        #         if spells[i] * potions[j] >= success:
        #             pairs[i] += 1
        #             continue

        # return pairs
