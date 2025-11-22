class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            temp = nums[i] % 3
            if abs(temp) > 1:
                count += 1
            else:
                count += temp
        return count