class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s = list(s)
        l , r = 0 , k-1
        while l < r:
            s[r] ,s[l] = s[l], s[r]
            r -= 1
            l += 1
        return "".join(s)