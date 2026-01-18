class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Prefix sums
        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]

        def row_sum(r, c1, c2):
            return row[r][c2] - row[r][c1]

        def col_sum(c, r1, r2):
            return col[r2][c] - col[r1][c]

        max_k = min(m, n)
        for k in range(max_k, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row_sum(i, j, j + k)

                    # Check rows
                    if any(row_sum(i + x, j, j + k) != target for x in range(k)):
                        continue

                    # Check columns
                    if any(col_sum(j + x, i, i + k) != target for x in range(k)):
                        continue

                    # Check diagonals
                    d1 = sum(grid[i + x][j + x] for x in range(k))
                    d2 = sum(grid[i + x][j + k - 1 - x] for x in range(k))

                    if d1 == target and d2 == target:
                        return k

        return 1