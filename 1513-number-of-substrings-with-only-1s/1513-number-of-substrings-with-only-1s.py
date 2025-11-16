class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        current = 0
        
        for ch in s:
            if ch == '1':
                current += 1
                count += current
            else:
                current = 0
        
        return count % MOD