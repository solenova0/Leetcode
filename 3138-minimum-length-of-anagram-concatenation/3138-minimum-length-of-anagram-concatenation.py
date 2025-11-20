class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)

        for L in range(1, n + 1):
            if n % L != 0:
                continue

            block = s[:L]                     
            sorted_block = sorted(block)
            valid = True

           
            for i in range(0, n, L):
                if sorted(s[i:i+L]) != sorted_block:
                    valid = False
                    break

            if valid:
                return L

        return n