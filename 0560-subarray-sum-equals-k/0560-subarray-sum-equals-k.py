class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        freq = defaultdict(int)
        freq[0] = 1   
        
        curr_sum = 0
        count = 0
        
        for x in nums:
            curr_sum += x
            
           
            count += freq[curr_sum - k]
            
            freq[curr_sum] += 1
        
        return count