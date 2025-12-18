class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        x , y = 0, 0

        for i in range(len(points)):
            x = max(x, points[i][0])
            y = max(y, points[i][1])
        return x * y / 2

        