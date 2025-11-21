class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i not in mapping:
                stack.append(i)
            else:
                if not stack:
                    return False 
                else:
                    popped = stack.pop()
                    if popped != mapping[i]:
                        return False
        return not stack
