class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr_longest = 0
        set1 = set()
        for r in range(len(s)):
            while s[r] in set1:
                set1.remove(s[l])
                l += 1
        
            set1.add(s[r])
            curr_longest = max(curr_longest, r - l + 1)
        return curr_longest

        # dic = {}
        # l = 0
        # longest = 0
        # for r in range(len(s)):
        #     if s[r] in dic and dic[s[r]] >= l:
        #         l = dic[s[r]] + 1
        #     dic[s[r]] = r
        #     longest = max(longest, r - l +1)  
        # return longest 
