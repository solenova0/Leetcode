class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
    
        total_happiness = 0
        for i in range(k):
            current_val = happiness[i] - i
            
            if current_val > 0:
                total_happiness += current_val
            else:
                break
                
        return total_happiness