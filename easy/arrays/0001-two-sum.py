from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Находим самое короткое слово
        small_st = strs[0]
        for word in strs[1:]:
            if len(small_st) > len(word):
                small_st = word

        # Сравниваем каждую позицию
        result = ""
        for i in range(len(small_st)):
            for word in strs:
                if word[i] != small_st[i]:
                    return result
            result += small_st[i]

        return result


# Time Complexity: O(S), где S — сумма длин всех строк в худшем случае
# Space Complexity: O(1), так как храним только результирующую строку
