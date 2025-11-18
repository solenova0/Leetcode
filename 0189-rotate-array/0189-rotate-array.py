class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n < k:
            k = k % n
        if n < 2:
            return    
        l = 0 
        r = n - 1
        while l < r :
            nums[r],nums[l] = nums[l],nums[r]
            l += 1
            r -= 1
        l = 0
        r = k - 1
        while l < r :
            nums[r] , nums[l] = nums[l] , nums[r]
            l += 1
            r -= 1

        l = k 
        r = n - 1
        while l < r :
            nums[r] , nums[l] = nums[l] , nums[r]
            l += 1
            r -= 1
