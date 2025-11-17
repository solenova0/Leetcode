class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        i = len(matrix)
        j = len(matrix[0])
        result = [[0] * i for _ in range(j)]

        for r in range(i):
            for c in range(j):
                result[c][r] = matrix[r][c]

        return result