from typing import List
from collections import Counter

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = Counter({0: 1})  # Stores count of prefix sums
        ans = t = 0  # t = number of odd numbers seen so far
        for v in nums:
            t += v % 2  # +1 if odd, +0 if even
            ans += cnt[t - k]  # Add number of times (t - k) has occurred
            cnt[t] += 1  # Record current number of odd numbers
        return ans
