import heapq

# 다익스트라
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    
    for time in times:
        graph[time[0]].append(time[1:])
    
    INF = int(1e9)
    dist = [INF]*(n)

    dist[k-1] = 0
    q = []
    heapq.heappush(q, (0, k))
    
    while q:
        dist_now, now = heapq.heappop(q)
        for node in graph[now]:
            cost = dist_now + node[1]
            if cost < dist[node[0]-1]:
                dist[node[0]-1] = cost
                heapq.heappush(q, (cost, node[0]))
    
    result = max(dist)
    return result if result < INF else -1


# 책의 풀이: dist 배열을 사용하지 않고 힙의 특성을 이용해 구함
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    
    for u, v, w in times:
        graph[u].append((v, w))
    
    q = []
    heapq.heappush(q, (0, k))
    
    dist = collections.defaultdict(int)

    while q:
        time, node = heapq.heappop(q)
        # 힙에서 꺼내기 때문에 값이 존재한다면 그 값은 이미 최솟값임
        # 따라서 값이 존재하지 않을 때만 연산
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                cost = time + w
                heapq.heappush(q, (cost, v))
    
    if len(dist) == n:
        return max(dist.values())
    return -1