class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        total = 0
        expected = sorted(heights)
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                total += 1
        return total