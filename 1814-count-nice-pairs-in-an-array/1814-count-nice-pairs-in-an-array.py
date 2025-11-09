class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def rev(x):
            return int(str(x)[::-1])

        freq = {}
        ans = 0
        
        for x in nums:
            v = x - rev(x)
            ans += freq.get(v, 0)
            freq[v] = freq.get(v, 0) + 1
        
        return ans % MOD