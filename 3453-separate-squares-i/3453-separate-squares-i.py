class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        area = sum(l * l for x, y, l in squares)
        target = area / 2
        
        low = min(y for x, y, l in squares)
        high = max(y + l for x, y, l in squares)
        
        for _ in range(100):
            mid = (low + high) / 2
            
            current_area = 0
            for x, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    current_area += l * l
                else:
                    current_area += (mid - y) * l
            
            if current_area < target:
                low = mid
            else:
                high = mid
                
        return low