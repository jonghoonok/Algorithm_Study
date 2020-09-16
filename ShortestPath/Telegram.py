import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(c)

cnt = 0
max_time = 0
for node in distance:
    if node == INF or node == 0:
        continue
    else:
        cnt += 1
        if node > max_time:
            max_time = node

print(cnt, max_time)