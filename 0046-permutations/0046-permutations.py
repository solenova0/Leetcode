class Solution(object):
      def permute(self, nums):
         
         res = [[]]
         for i in range(len(nums)):
             cache = set()
             while len(res[0]) == i:
                 curr = res.pop(0)
                 for j in range(len(curr) + 1):
                     
                     new_perm = curr[:j] + [nums[i]] + curr[j:]
                     stemp = ''.join(map(str, new_perm))
                     if stemp not in cache:
                         cache.add(stemp)
                         res.append(new_perm)
         return res