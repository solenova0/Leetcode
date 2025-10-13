class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        a , b = 0 , 0
        while a < len(word1) and b < len(word2):
            s.append(word1[a])
            s.append(word2[b])
            a += 1
            b += 1
        s.append(word1[a:])
        s.append(word2[b:])
        return "".join(s)
    
        