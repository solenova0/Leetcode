class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        m = 1
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                count = 1
            
            if i >= k - 1:
                if count >= k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)
        
        return ans