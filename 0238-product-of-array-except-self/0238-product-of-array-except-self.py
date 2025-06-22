class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        # Calculate prefix products and store in result
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # Calculate suffix products and multiply with result
        suffix = 1
        for i in reversed(range(n)):
            res[i] *= suffix
            suffix *= nums[i]

        return res
