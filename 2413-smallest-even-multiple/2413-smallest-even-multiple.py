class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:return abs(n)
        else: return abs(2 * n)
        