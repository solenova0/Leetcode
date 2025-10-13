class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i, j = 0, 0 
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1  
        #     j += 1      
        # return i == len(s)  
        T = len(t)
        S = len(s)
        if s == '' : return True
        if T < S: return False
        
        j = 0
        for i in range(T):
            if s[j] == t[i]:
                if j == S -1:
                    return True
                j += 1

        return False
