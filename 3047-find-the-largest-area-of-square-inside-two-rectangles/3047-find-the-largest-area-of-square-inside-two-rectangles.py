class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0
        
        for i in range(n):
            x1a, y1a = bottomLeft[i]
            x2a, y2a = topRight[i]
            for j in range(i+1, n):
                x1b, y1b = bottomLeft[j]
                x2b, y2b = topRight[j]
                
                w = min(x2a, x2b) - max(x1a, x1b)
                # Intersection height
                h = min(y2a, y2b) - max(y1a, y1b)
                
                if w > 0 and h > 0:
                    side = min(w, h)
                    max_area = max(max_area, side * side)
        
        return max_area
