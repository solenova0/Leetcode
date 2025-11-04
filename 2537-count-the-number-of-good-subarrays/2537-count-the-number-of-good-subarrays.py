class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = 0
        pairs = 0
        res = 0
        
        for r, val in enumerate(nums):
            pairs += freq[val]  
            freq[val] += 1
            
            while pairs - (freq[nums[l]] - 1) >= k:
                pairs -= (freq[nums[l]] - 1)
                freq[nums[l]] -= 1
                l += 1
            
           
            if pairs >= k:
                res += l + 1
        
        return res