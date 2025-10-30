class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_length(ch):
            l = 0
            flips = 0
            ans = 0

            for r in range(len(answerKey)):
                if answerKey[r] != ch:
                    flips += 1

                while flips > k:
                    if answerKey[l] != ch:
                        flips -= 1
                    l += 1

                ans = max(ans, r - l + 1)

            return ans

        return max(max_length('T'), max_length('F'))
