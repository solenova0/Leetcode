class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        m = k // 2

        original_profit = 0
        original_profits = [0] * n
        
        for i in range(n):
            profit_i = strategy[i] * prices[i]
            original_profits[i] = profit_i
            original_profit += profit_i
            
        if n == k:
            modified_profit = 0
            
            for i in range(m, n):
                modified_profit += prices[i]
            
            return max(original_profit, modified_profit)
        current_increase = 0

        for i in range(m):
            current_increase += -original_profits[i]
        
        for i in range(m, k):
            current_increase += prices[i] - original_profits[i]

        max_increase = max(0, current_increase)
        
        for j in range(n - k):
            term_1 = original_profits[j]
            term_2 = -prices[j + m]
            term_3 = prices[j + k]
            term_4 = -original_profits[j + k]
            
            current_increase = current_increase + term_1 + term_2 + term_3 + term_4
            
            max_increase = max(max_increase, current_increase)
            
        return original_profit + max_increase