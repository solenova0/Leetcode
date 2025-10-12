class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_ones = 0
        window = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                num_ones += 1
                window = max(window , num_ones)
            else:
                num_ones = 0

        return window

            