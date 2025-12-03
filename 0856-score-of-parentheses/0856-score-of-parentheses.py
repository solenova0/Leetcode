class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        for c in s:
            if c == ")":
                score += 1
        return score