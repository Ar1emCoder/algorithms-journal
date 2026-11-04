class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            d = 1
            curr_load = 0  # вес груза текущего корабля
            for w in weights:
                if curr_load + w > capacity:
                    d += 1
                    curr_load = w
                else:
                    curr_load += w
            return d <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left


# Time Complexity: O(N * log(sum(weights))), где N - длина weights
# Space Complexity: O(1)
