class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)

        window = n - k

        curr = sum(cardPoints[:window])
        min_window = curr

        for i in range(window, n):
            curr += cardPoints[i] - cardPoints[i - window]
            min_window = min(min_window, curr)

        return total - min_window