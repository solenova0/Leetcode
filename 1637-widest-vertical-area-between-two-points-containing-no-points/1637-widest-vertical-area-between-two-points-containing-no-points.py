class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
      sorted_x = sorted({x for x, y in points})
        return max([b-a for a, b in itertools.izip(sorted_x, sorted_x[1:])] + [0])