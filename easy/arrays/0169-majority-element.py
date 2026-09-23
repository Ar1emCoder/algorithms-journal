from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Подсчёт частот через словарь
        ans = {}
        for num in nums:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1

        # Возвращаем элемент с максимальной частотой
        return max(ans, key=ans.get)


# Time Complexity: O(n) - один проход + поиск максимума
# Space Complexity: O(n) - словарь для подсчёта частот
