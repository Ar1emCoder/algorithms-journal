class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        pred_pred = nums[0]
        pred = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(pred_pred + nums[i], pred)
            pred_pred = pred
            pred = curr
        return pred


# Time Complexity: O(N) - где N длина массива nums. Мы делаем один проход по массиву.
# Space Complexity: O(1) - мы не создаем массив dp размером N, а храним только два предыдущих состояния (pred_pred и pred).
