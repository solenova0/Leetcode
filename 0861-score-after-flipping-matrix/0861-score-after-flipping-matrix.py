class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        result = 0
        for j in range(n):
            ones = sum(grid[i][j] for i in range(m))
            max_ones = max(ones, m - ones)
            result += max_ones * (1 << (n - j - 1))

        return result

        