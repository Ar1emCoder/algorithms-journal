class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        pred_pred = 1
        pred = 1
        for i in range(2, n + 1):
            curr = pred_pred + pred
            pred_pred = pred
            pred = curr
        return pred


# Time Complexity: O(N) - мы делаем один проход циклом от 2 до n.
# Space Complexity: O(1) - мы используем только три переменные (pred_pred, pred, curr), независимо от размера входных данных n.
