class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_categories = ["electronics","grocery","pharmacy","restaurant"]
        valid = []
        
        for i in range(len(code)):
            if not code[i] or any(not (c.isalnum() or c == '_') for c in code[i]):
                continue
            if businessLine[i] in valid_categories and isActive[i]:
                valid.append((businessLine[i], code[i]))
        
        valid.sort(key=lambda x: (
            valid_categories.index(x[0]),
            x[1]
        ))
        
        return [c for _, c in valid]
