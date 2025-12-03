class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque(range(n))  
        time = 0
        
        while True:
            i = q.popleft()   
            tickets[i] -= 1   
            time += 1
            
            if i == k and tickets[i] == 0:
                return time 
            
            if tickets[i] > 0:
                q.append(i)   