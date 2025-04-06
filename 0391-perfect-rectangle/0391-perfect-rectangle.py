from typing import List
from collections import defaultdict

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        point_count = defaultdict(int)
        minX = minY = float('inf')
        maxX = maxY = float('-inf')
        actual_area = 0

        for x1, y1, x2, y2 in rectangles:
            # Update bounding box
            minX, minY = min(minX, x1), min(minY, y1)
            maxX, maxY = max(maxX, x2), max(maxY, y2)
            
            # Add area of current rectangle
            actual_area += (x2 - x1) * (y2 - y1)

            # Count the 4 corners
            for point in [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]:
                point_count[point] ^= 1  # XOR flip: adds if new, removes if duplicate

        # Expected area from the bounding box
        expected_area = (maxX - minX) * (maxY - minY)

        # There must be exactly 4 corner points left
        expected_corners = {(minX, minY), (minX, maxY), (maxX, maxY), (maxX, minY)}
        if actual_area != expected_area or set(p for p, v in point_count.items() if v) != expected_corners:
            return False

        return True
