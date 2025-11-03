class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        sub_sums = []
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                sub_sums.append(curr)
        sub_sums.sort()
        result = sum(sub_sums[left-1 : right]) % mod
        return result
    #    Time: O(n² log n)
    #    Space: O(n²)