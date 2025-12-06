class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        count = 0
        curr_max = 0
        for r in range(n):
            if nums[r] == 0:
                count += 1
             
            while count > 0:
                if nums[l] == 0:
                    count -= 1
                l += 1
            curr_max = max(curr_max,r - l + 1)
        return curr_max