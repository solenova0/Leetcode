class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        squared = [0] * n
        l, r = 0, n - 1
        i = n - 1

        while l <= r:
            left_sq = nums[l] ** 2
            right_sq = nums[r] ** 2
            if left_sq > right_sq:
                squared[i] = left_sq
                l += 1
            else:
                squared[i] = right_sq
                r -= 1
            i -= 1

        return squared
        