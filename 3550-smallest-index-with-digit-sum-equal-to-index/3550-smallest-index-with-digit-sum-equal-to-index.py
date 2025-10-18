class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            s = 0
            n = num
            while n > 0:
                s += (n % 10)
                n //= 10
            if s == i:
                return i
        return -1