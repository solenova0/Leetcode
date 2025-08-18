from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        longest_palindrome_length = 0
      
        for count in char_count.values():
           longest_palindrome_length += count - (count % 2)
           longest_palindrome_length += ((longest_palindrome_length % 2 == 0) and (count % 2 == 1))
      
        return longest_palindrome_length