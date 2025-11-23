class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        seen = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        count = 0
        curr_max = 0

        for right in range(len(s)):
            if s[right] in seen:
                count += 1

            if right - left + 1 == k:
                curr_max = max(curr_max, count)

                if s[left] in seen:
                    count -= 1
                left += 1

        return curr_max