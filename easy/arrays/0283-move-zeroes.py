from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Указатель для позиции следующего ненулевого элемента
        insert_pos = 0

        # Первый проход: перемещаем все ненулевые элементы в начало
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Второй проход: заполняем оставшиеся позиции нулями
        for i in range(insert_pos, len(nums)):
            nums[i] = 0


# Time Complexity: O(n) - два прохода по массиву
# Space Complexity: O(1) - модифицируем in-place
