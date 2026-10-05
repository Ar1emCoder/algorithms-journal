class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]

        pred_pred = cost[0]
        pred = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(pred_pred, pred)
            pred_pred, pred = pred, curr

        return min(pred_pred, pred)


# Time Complexity: O(N) - делаем два прохода по массиву (для двух случаев).
# Space Complexity: O(1) - используем индексы вместо срезов, не создавая копий массива.
