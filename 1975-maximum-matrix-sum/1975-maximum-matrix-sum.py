class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        neg_count = 0
        min_abs_val = float('inf')
        
        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    neg_count += 1
                min_abs_val = min(min_abs_val, abs(val))
                
        if neg_count % 2 == 1:
            return total_sum - 2 * min_abs_val
        
        return total_sum