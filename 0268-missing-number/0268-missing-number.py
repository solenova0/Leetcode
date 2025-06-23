class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        # ensure n is at the last index
        if nums[-1] !=len(nums):
          return len(nums)
        # ensure 0 is at the first index
        elif nums[0] != 0:
          return 0
        
        # otherwise, the missing number is in the range (0, n)
        for i in range(1, len(nums)):
          expected_num = nums[i-1] + 1
          if nums[i] != expected_num:
            return expected_num