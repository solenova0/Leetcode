class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i , x in enumerate(nums):
            need = target - x
            if need in dict1:
                return [dict1[need] , i]
            dict1[x] = i
        