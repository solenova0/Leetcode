class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minm = min(nums)
        moves = 0
        for i in range(len(nums)):
            moves += nums[i] - minm
        return moves