class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0
        curr_sum = 0
        for right in range(len(nums)):           #Time: O(n)
            curr_sum += nums[right]              #Space: O(1)

            while curr_sum >= target:
                min_len = min(min_len, right - left +1)
                curr_sum -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len