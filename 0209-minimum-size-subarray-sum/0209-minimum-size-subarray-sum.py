class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l = 0
        curr_sum = 0
        for r in range(len(nums)):           #Time: O(n)
            curr_sum += nums[r]              #Space: O(1)

            while curr_sum >= target:
                min_len = min(min_len, r - l +1)
                curr_sum -= nums[l]
                l += 1
        return 0 if min_len == float('inf') else min_len