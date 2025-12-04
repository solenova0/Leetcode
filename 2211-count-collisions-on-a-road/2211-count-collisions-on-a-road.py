class Solution:
    def countCollisions(self, directions: str) -> int:
            i = 0
            n = len(directions)
            while i < n and directions[i] == 'L':
                i += 1
            
            j = n - 1
            while j >= 0 and directions[j] == 'R':
                j -= 1
            
            count = 0
            for k in range(i, j + 1):
                if directions[k] != 'S':
                    count += 1
            
            return count