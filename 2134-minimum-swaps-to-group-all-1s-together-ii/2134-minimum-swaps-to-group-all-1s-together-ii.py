class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_ones = nums.count(1)
        nums = nums + nums 
        count_zeros, curr_zeros = float('inf'), 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                curr_zeros += 1

            # When window size equals total ones
            if r - l + 1 == count_ones:
                count_zeros = min(count_zeros, curr_zeros)
                if nums[l] == 0:
                    curr_zeros -= 1
                l += 1

        return 0 if count_zeros == float('inf') else count_zeros