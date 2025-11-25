class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lefttopivot = []
        righttopivot = []
        middle = []
        
        
        for x in nums:
            if x > pivot:
                righttopivot.append(x)
            elif x < pivot:
                lefttopivot.append(x)
            else:
                middle.append(x)

        result = []
        
       
        for i in range(len(lefttopivot)):
            result.append(lefttopivot[i])
        for i in range(len(middle)):
            result.append(middle[i])
        for i in range(len(righttopivot)):
            result.append(righttopivot[i])
           

        return result