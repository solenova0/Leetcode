class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for i, value in enumerate(nums):
            if value in seen and i - seen[value] <= k:
                return True
            seen[value] = i
        return False