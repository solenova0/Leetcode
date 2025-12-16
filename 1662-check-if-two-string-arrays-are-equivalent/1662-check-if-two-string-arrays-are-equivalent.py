class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp1 = ""
        temp2 = ""
        for n in word1:
            temp1 += n
        for m in word2:
            temp2 += m
        return temp1 == temp2
            
        