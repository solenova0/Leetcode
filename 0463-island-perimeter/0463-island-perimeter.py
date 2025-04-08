class Solution(object):
    def islandPerimeter(self, grid):
        ret = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        ret += 1
                    if i + 1 == m or grid[i + 1][j] == 0:
                        ret += 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        ret += 1
                    if j + 1 == n or grid[i][j + 1] == 0:
                        ret += 1
        return ret
