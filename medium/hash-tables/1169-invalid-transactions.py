from collections import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        history = {}
        added = set()

        for i, trans in enumerate(transactions):
            name, time, amount, city = trans.split(",")
            time, amount = int(time), int(amount)

            if amount > 1000:
                added.add(i)

            if name in history:
                for old_name, old_time, old_amount, old_city, old_idx in history[name]:
                    if abs(time - old_time) <= 60 and city != old_city:
                        added.add(i)
                        added.add(old_idx)

            if name not in history:
                history[name] = []
            history[name].append((name, time, amount, city, i))

        result = [transactions[i] for i in added]
        return result


# Time Complexity: O(n²) — для каждой транзакции проверяем все предыдущие того же человека. - те, что в history[name]
# Space Complexity: O(n) — храним историю транзакций и множество добавленных индексов.
