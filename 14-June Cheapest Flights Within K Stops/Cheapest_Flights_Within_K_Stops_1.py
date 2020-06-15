class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst: 
            return 0
        
        dictionary = collections.defaultdict(list)
        visited = collections.defaultdict(lambda: float('inf'))
        
        for u, v, p in flights:
            dictionary[u] += [(v, p)]
    
        q = [(src, -1, 0)]
        
        while q:
            pos, k, cost = q.pop(0)
            if pos == dst or k == K: continue 
            for nei, p in dictionary[pos]:
                if cost + p >= visited[nei]:
                    continue
                else:
                    visited[nei] = cost+p
                    q += [(nei, k+1, cost+p)]
                
        return visited[dst] if visited[dst] < float('inf') else -1
