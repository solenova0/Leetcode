class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        boxes = 1
        capacity_total = 0
        for i in range(len(capacity)):
            capacity_total += capacity[i]
            if capacity_total >= total:
                return boxes
            
            boxes += 1

        