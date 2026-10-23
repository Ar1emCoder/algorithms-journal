class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += (mid + pile - 1) // mid

            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left


# Time Complexity: O(n * log(max_pile)), где n - количество кучек. Бинарный поиск по диапазону [1, max(piles)] занимает O(log(max_pile)), а проверка каждой скорости требует O(n).
# Space Complexity: O(1) - используем только константную память.
