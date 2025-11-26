class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        lists = []
        for x in nums:
            if not lists or lists[-1] != x:
                lists.append(x)
        count = 0
        for i in range(1, len(lists)-1):
            if lists[i] > lists[i - 1] and lists[i] > lists[i + 1]:
                count += 1
            elif lists[i] < lists[i - 1] and lists[i] < lists[i + 1]:
                count += 1
        return count




