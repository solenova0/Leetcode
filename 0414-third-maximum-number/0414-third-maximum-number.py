class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        count = 1 
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] != nums[i+1]:
                count += 1
            if count == 3:
                return nums[i]
            i -= 1
        return max(nums)