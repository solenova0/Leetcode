class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_l = float('inf')
        summ = 0

        for r in  range(len(nums)):
            summ += nums[r]
            while summ >= target:
                summ -= nums[l]
                min_l = min(min_l , r - l + 1)
                l += 1
        return 0 if min_l == float('inf') else min_l

