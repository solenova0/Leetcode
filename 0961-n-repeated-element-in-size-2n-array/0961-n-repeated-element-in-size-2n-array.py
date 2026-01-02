class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
            n = len(nums)
            seen = set()
            for i in range(n):
                if nums[i] in seen:
                    return nums[i]
                seen.add(nums[i])
        