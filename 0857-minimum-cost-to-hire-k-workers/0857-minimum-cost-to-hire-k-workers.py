class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        
        min_cost = float('inf')
        current_quality_sum = 0
        max_heap = []
        
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            current_quality_sum += q
            
            if len(max_heap) > k:
                current_quality_sum += heapq.heappop(max_heap)
            
            if len(max_heap) == k:
                min_cost = min(min_cost, ratio * current_quality_sum)
                
        return float(min_cost)