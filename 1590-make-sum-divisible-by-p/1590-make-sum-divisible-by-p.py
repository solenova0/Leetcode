class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0

        prefix = 0
        seen = {0: -1}   # prefix_mod : index
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            needed = (prefix - target) % p

            if needed in seen:
                res = min(res, i - seen[needed])

            seen[prefix] = i

        return res if res < len(nums) else -1