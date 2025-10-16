class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted([(num, i) for i, num in enumerate(nums)])
        left, right = 0, len(arr) - 1
        
        while left < right:
            total = arr[left][0] + arr[right][0]
            if total == target:
                return [arr[left][1], arr[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1