class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            total = left * left + right * right
            if total == c:                             #Time : O(radical c)
                return True                            #Space : O(1)
            elif total < c:
                left += 1
            else:
                right -= 1
        return False
