class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0 
        zeros = 0
        min_len = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            min_len = max(min_len , r - l)
        return min_len
        