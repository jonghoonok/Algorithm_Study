# O(VlogE)의 복잡도를 갖는 알고리즘

import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    # 각 노드의 최단거리를 "업데이트"하는 데 사용하는 우선순위큐
    q = []
    heapq.heappush(q, (0, start))
    # 출발점으로부터의 각 노드의 최단거리를 저장하는 배열: 최종 결과
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 우선순위 큐는 거리가 짧은 것부터 먼저 처리함
        # 같은 노드에 대해 거리가 더 짧은 경로를 처리했다면 다음부터는 처리할 필요 없음
        # dist가 갖고 있는 정보(큐에 저장된 거리)와 distance(처리된 거리)를 비교
        if distance[now] < dist:
            continue
        # now의 주변 노드들을 탐색
        for edge in graph[now]:
            cost = dist + edge[1]
            if cost < distance[edge[0]]:
                distance[edge[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])