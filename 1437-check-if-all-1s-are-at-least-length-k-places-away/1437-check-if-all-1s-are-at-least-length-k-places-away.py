class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k   
        for right in range(len(nums)):
            if nums[right] == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1

        return True
