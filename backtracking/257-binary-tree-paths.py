from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def backtrack(nood, cur_path):
            if not nood:
                return

            cur_path.append(str(nood.val))

            if not nood.left and not nood.right:
                res.append("->".join(cur_path))
            else:
                backtrack(nood.left, cur_path)
                backtrack(nood.right, cur_path)

            cur_path.pop()

        backtrack(root, [])
        return res


# Time Complexity: O(n) — посещаем каждый узел один раз
# Space Complexity: O(n) — глубина стека рекурсии
