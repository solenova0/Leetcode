class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_map = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}

        state = 0                   
        first_occurrence = {0: -1}   
        longest = 0

        for i, ch in enumerate(s):
            if ch in vowel_map:
                bit = vowel_map[ch]
                state ^= (1 << bit) 
            if state in first_occurrence:
                longest = max(longest, i - first_occurrence[state])
            else:
                first_occurrence[state] = i
        
        return longest