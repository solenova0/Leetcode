class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        pos_idx = 0     
        neg_idx = 1      
        
        for x in nums:
            if x > 0:
                result[pos_idx] = x
                pos_idx += 2
            else:
                result[neg_idx] = x
                neg_idx += 2
        
        return result