class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        rev_adj = [[] for _ in range(n)]
        
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))
        dist = [[float('inf')] * 2 for _ in range(n)]
        pq = [(0, 0, 0)]  
        dist[0][0] = 0
        
        while pq:
            d, u, switched = heapq.heappop(pq)
            
            if d > dist[u][switched]:
                continue
            
            if u == n - 1:
                return d
                
            # 1. Standard Move: u -> v
            for v, w in adj[u]:
                if dist[v][0] > d + w:
                    dist[v][0] = d + w
                    heapq.heappush(pq, (dist[v][0], v, 0))
            
            if not switched:
                for v, w in rev_adj[u]:
                    if dist[v][0] > d + 2 * w:
                        dist[v][0] = d + 2 * w
                        
                        heapq.heappush(pq, (dist[v][0], v, 0))
                        
        ans = min(dist[n-1])
        return ans if ans != float('inf') else -1