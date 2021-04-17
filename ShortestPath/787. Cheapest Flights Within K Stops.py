import collections
import heapq

def findCheapestPrice(n: int, flights, src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        q = []
        k = 0
        heapq.heappush(q, (0, src, k))
        
        while q:
            price, node, k = heapq.heappop(q)
            if node == dst:
                return price
            if k <= K:
                k += 1
                for v, w in graph[node]:
                    cost = price + w
                    heapq.heappush(q, (cost, node, k))
        return -1

print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))