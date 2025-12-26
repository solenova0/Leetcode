class Solution:
    def bestClosingTime(self, customers: str) -> int:
        profit = 0
        maxProfit = 0
        minPenalty = 0
        for i,c in enumerate(customers):
            profit += (1 if c =='Y' else -1)
            if profit > maxProfit:
                maxProfit = profit
                minPenalty = i + 1
        return minPenalty

        