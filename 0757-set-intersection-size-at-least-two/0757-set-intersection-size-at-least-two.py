class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = -1
        b = -1
        count = 0

        for l, r in intervals:
            if l <= a:
                continue
            elif l <= b:     
                count += 1
                a, b = b, r
            else:
                count += 2
                a, b = r-1, r

        return count