class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        result = []
        start = 0
        end = 0

        for i in range(len(s)):
            ch = s[i]
            end = max(end, last[ch])

            if i == end:    
                result.append(end - start + 1)
                start = i + 1

        return result


            