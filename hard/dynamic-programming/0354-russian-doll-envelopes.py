from typing import List
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h[1] for h in envelopes]
        tails = []

        for h in heights:
            indx = bisect.bisect_left(tails, h)
            if indx == len(tails):
                tails.append(h)
            else:
                tails[indx] = h
        return len(tails)


# Time Complexity: O(n log n) — сортировка O(n log n) + цикл с бинарным поиском O(n log n)
# Space Complexity: O(n) — массив tails для хранения последовательности
