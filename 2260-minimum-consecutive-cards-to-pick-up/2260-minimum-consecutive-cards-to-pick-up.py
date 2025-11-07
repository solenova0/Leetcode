class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index = {}
        ans = float('inf')

        for i, card in enumerate(cards):
            if card in last_index:
                ans = min(ans, i - last_index[card] + 1)
            last_index[card] = i
        
        return ans if ans != float('inf') else -1