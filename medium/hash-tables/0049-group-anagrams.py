from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in result:
                result[key] = [word]
            else:
                result[key].append(word)

        return list(result.values())


# Time Complexity: O(n * k log k) — n слов, каждое сортируется за O(k log k), где k — длина слова
# Space Complexity: O(n * k) — хранение всех слов в хеш-таблице
