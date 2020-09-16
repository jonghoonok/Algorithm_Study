import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)        
        if price[now] < dist:
            continue
        for city in graph[now]:
            cost = dist + city[1]
            if cost < price[city[0]]:
                price[city[0]] = cost
                heapq.heappush(q, (cost, city[0]))


input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
price = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, goal = map(int, input().split())

dijkstra(start)

print(price[goal])