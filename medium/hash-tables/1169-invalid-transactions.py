from collections import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        history = {}
        added = set()  # отслеживаем индексы или сами транзакции

        for i, trans in enumerate(transactions):
            name, time, amount, city = trans.split(",")
            time = int(time)
            amount = int(amount)

            if amount > 1000:
                if i not in added:
                    result.append(trans)
                    added.add(i)

            if name in history:
                for old_time, old_city, old_trans, old_idx in history[name]:
                    if abs(time - old_time) <= 60 and city != old_city:
                        if i not in added:
                            result.append(trans)
                            added.add(i)
                        if old_idx not in added:
                            result.append(old_trans)
                            added.add(old_idx)

            if name not in history:
                history[name] = []
            history[name].append((time, city, trans, i))

        return result


# Time Complexity: O(n²) — для каждой транзакции проверяем все предыдущие того же человека.
# Space Complexity: O(n) — храним историю транзакций и множество добавленных индексов.
