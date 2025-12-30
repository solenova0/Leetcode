class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r + 1][c + 1] != 5:
                    continue
                
                if self.is_magic(grid, r, c):
                    count += 1
        return count

    def is_magic(self, grid, r, c):
        vals = [grid[r+i][c+j] for i in range(3) for j in range(3)]
        if sorted(vals) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        
       #Rows
        if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or
            grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15):
            return False
            
        # Columns
        if (grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or
            grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15):
            return False
            
        # Diagonals
        if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
            grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
            return False
            
        return True