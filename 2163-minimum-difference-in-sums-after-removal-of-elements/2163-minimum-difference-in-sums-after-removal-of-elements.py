class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total_len = len(nums)
        ans = math.inf

        # maxHeap is used to keep track of the n smallest possible left numbers (stored as negatives)
        maxHeap = []
        leftSum = 0
        minLeftSum = [0] * total_len  # minLeftSum[i]: min sum of n elements from nums[0..i]

        # Step 1: Traverse from left to 2n to fill minLeftSum
        for i in range(2 * n):
            heapq.heappush(maxHeap, -nums[i])  # max heap by pushing negative values
            leftSum += nums[i]
            if len(maxHeap) > n:
                leftSum += heapq.heappop(maxHeap)  # remove largest (smallest negative)
            if len(maxHeap) == n:
                minLeftSum[i] = leftSum

        # Step 2: Traverse from right to n to find min difference
        minHeap = []
        rightSum = 0

        for i in range(total_len - 1, n - 1, -1):
            heapq.heappush(minHeap, nums[i])  # min heap for largest right-side elements
            rightSum += nums[i]
            if len(minHeap) > n:
                rightSum -= heapq.heappop(minHeap)  # remove smallest
            if len(minHeap) == n:
                # Compare with previously computed minLeftSum
                ans = min(ans, minLeftSum[i - 1] - rightSum)

        return ans