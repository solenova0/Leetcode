class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7

        # dp[j] = number of ways to reach sum j using some subset of {1^x, 2^x, ..., i^x}
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            val = pow(i, x)
            if val > n:
                # This i cannot contribute to any sum <= n, skip updating
                continue
            # update in reverse to ensure each i is used at most once
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % mod

        return dp[n]