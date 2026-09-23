from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Минимальная цена покупки
        min_price = float("inf")
        # Максимальная прибыль
        max_profit = 0

        for price in prices:
            # Если нашли цену ниже — обновляем минимум
            if price < min_price:
                min_price = price
            # Иначе считаем прибыль и обновляем максимум
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# Time Complexity: O(n) - один проход по массиву
# Space Complexity: O(1) - две переменные
