class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lists = []
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            lists.append(cur_sum)
        return lists

