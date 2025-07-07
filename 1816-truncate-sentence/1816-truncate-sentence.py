class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for i in range(len(s)):
            if s[i] == ' ':
                k -= 1
                if not k:
                    return s[:i]
        return s
