class Solution:
    def atMost(self, nums, k):
        if k < 0:
            return 0

        count = {}
        left = 0
        res = 0

        for right, val in enumerate(nums):
            count[val] = count.get(val, 0) + 1

            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            res += right - left + 1

        return res

    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        return self.atMost(nums, k) - self.atMost(nums, k - 1)