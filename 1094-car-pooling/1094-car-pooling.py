class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # time = [0] * 1001
        
        # for passengers, i, j in trips:
        #     time[i] += passengers
        #     time[j] -= passengers
        
        # curr_passenger = 0
        # for k in time:
        #     curr_passenger += k
        #     if curr_passenger > capacity:
        #         return False
                
        # return True
        max_dist = 0
        for _, _, end in trips:
            max_dist = max(max_dist, end)
        
        stops = [0] * (max_dist + 1)
        
        for num, start, end in trips:
            for i in range(start, end):
                stops[i] += num
                if stops[i] > capacity:
                    return False
                    
        return True