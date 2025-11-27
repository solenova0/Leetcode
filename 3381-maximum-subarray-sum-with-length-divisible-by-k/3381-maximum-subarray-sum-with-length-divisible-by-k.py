class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        s = 0                  
        best = -10**18         
        mp = {0: 0}            

        for i, v in enumerate(nums, 1):
            s += v
            m = i % k

            if m in mp:
                best = max(best, s - mp[m])
            else:
                mp[m] = s

            mp[m] = min(mp[m], s)

        return best