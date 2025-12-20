class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows= len(strs)
        
        count = 0
        
        for j in range(cols):
            for i in range(1, rows):
                if strs[i-1][j] > strs[i][j]:
                    count += 1
                    break
                
                    
        return count
            