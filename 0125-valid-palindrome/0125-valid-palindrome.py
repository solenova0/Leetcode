class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
      
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
      
        # If we haven't found any mismatches, then it's a palindrome.
        return True