from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(index, cur_path):
            if index == len(s):
                res.append("".join(cur_path))
                return

            char = s[index]
            if char.isdigit():
                cur_path.append(char)
                backtrack(index + 1, cur_path)
                cur_path.pop()
            else:
                cur_path.append(char.lower())
                backtrack(index + 1, cur_path)
                cur_path.pop()

                cur_path.append(char.upper())
                backtrack(index + 1, cur_path)
                cur_path.pop()

        backtrack(0, [])
        return res


# Time Complexity: O(2^n * n) — для каждой буквы 2 варианта, n — длина строки
# Space Complexity: O(n) — глубина стека рекурсии
