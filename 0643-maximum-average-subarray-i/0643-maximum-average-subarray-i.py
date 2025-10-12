class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        curr_max = sum
        for r in range(k , len(nums)):
            sum += nums[r] - nums[r-k]
            curr_max = max(curr_max, sum )
        return curr_max / k
        