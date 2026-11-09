class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(weights, d, c):
            d = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > c:
                    d += 1
                    curr_weight = w
                else:
                    curr_weight += w

            return d <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            if can_ship(weights, days, mid):
                right = mid
            else:
                left = mid + 1

        return left


# Time Complexity: O(N * log(sum(weights))), где N - длина weights
# Space Complexity: O(1)
