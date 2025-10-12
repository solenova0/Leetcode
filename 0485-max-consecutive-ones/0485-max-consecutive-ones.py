class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        window = 0
        num_zeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            while num_zeros > 0:
                if nums[l] == 0:
                   num_zeros -= 1
                l += 1
            window = max(window , r - l + 1)
        return window

        