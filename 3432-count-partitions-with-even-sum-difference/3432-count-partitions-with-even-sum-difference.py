class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        curr_left = 0
        count = 0
        for i in range(0, n - 1):
            curr_left += nums[i]
            if (total - 2*curr_left) % 2 == 0:
                count += 1

        return count

        