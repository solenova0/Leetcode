class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        even = 1  
        odd = 0
        count = 0
        prefix = 0
        
        for num in arr:
            prefix = (prefix + num) % 2
            
            if prefix == 1:
                count = (count + even) % MOD
                odd += 1
            else:
                count = (count + odd) % MOD
                even += 1
        
        return count