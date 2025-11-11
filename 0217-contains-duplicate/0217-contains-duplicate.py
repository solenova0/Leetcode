class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = ()
        for i , value in enumerate(nums):
            if value in seen:
                return True
            seen.add(nums[i])
        return False

        


