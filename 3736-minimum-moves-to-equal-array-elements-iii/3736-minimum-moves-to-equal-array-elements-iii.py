class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        moves = 0
        for i in range(len(nums)):
            moves += maximum - nums[i]
        return moves
        