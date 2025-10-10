class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):                         # Compute prefix sums
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()                    # Deque will store indices of prefix sums
        min_length = float('inf')

        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return min_length if min_length != float('inf') else -1
