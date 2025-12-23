class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        time = [0] * 1001
        
        for passengers, i, j in trips:
            time[i] += passengers
            time[j] -= passengers
        
        curr_passenger = 0
        for k in time:
            curr_passenger += k
            if curr_passenger > capacity:
                return False
                
        return True