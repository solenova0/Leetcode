class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in map(chr, range(ord('a'), ord('z') + 1)):
            first = s.find(c)
            last = s.rfind(c)
            if first != -1 and last - first > 1:
                ans += len(set(s[first+1:last]))
        return ans