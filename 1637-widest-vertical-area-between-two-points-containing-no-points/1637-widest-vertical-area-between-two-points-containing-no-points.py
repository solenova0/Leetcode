from typing import List
import itertools  

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Extract unique x-coordinates and sort them
        sorted_x = sorted({x for x, y in points})
        # Calculate maximum difference between consecutive x-coordinates
        return max([b - a for a, b in zip(sorted_x, sorted_x[1:])] + [0])