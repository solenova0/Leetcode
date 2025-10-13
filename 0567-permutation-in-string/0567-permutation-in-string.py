class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        count1 = Counter(s1)
        count2 = Counter(s2[:n1])            #Time : O(n2)
                                             #Space : O(25) + O(25) = O(1) - Constant
        if count1 == count2:
            return True
        
        for i in range(n1, n2):
            count2[s2[i]] += 1
            left_char = s2[i - n1]
            count2[left_char] -= 1
            if count2[left_char] == 0:
                del count2[left_char]
            if count1 == count2:
                return True
        
        return False

        