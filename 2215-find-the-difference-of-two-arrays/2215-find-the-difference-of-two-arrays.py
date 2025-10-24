class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        result1 = []
        for x in set1:
            if x not in set2:
                result1.append(x)
        
        result2 = []
        for x in set2:
            if x not in set1:
                result2.append(x)
        
        return [result1, result2]