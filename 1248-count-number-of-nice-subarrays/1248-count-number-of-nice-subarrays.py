class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1

        curr = 0
        ans = 0

        for x in nums:
            curr += x % 2 
            ans += freq[curr - k]
            freq[curr] += 1

        return ans