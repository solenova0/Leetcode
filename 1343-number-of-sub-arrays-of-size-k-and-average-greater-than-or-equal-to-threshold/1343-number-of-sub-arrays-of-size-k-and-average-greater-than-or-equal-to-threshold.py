class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = sum(arr[:k])
        count = 0
        target = k * threshold
        if curr_sum >= target:
            count += 1
        
        left = 0
        for right in range(k, len(arr)):
            curr_sum += arr[right]
            curr_sum -= arr[left]
            left += 1
            if curr_sum >= target:
                count += 1
        return count