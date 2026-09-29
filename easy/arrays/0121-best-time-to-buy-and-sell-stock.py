class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = 1000000
        max_merge = 0
        for price in prices:
            min_price = min(price, min_price)
            merge = price - min_price
            max_merge = max(merge, max_merge)
        return max_merge


# Time Complexity: O(n) - один проход по массиву
# Space Complexity: O(1) - две переменные
