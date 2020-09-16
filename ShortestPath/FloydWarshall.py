# 모든 노드에 대해 모든 노드까지의 최단거리를 구하는 알고리즘
# O(V^3)
INF = int(1e9)
V = int(input())
E = int(input())
graph = [[INF]*(V+1) for _ in range(V+1)]

# 자기 자신으로 가는 거리는 0으로 초기화
for a in range(1, V+1):
    for b in range(1, V+1):
        if a == b:
            graph[a][b] = 0

# 노드 a에서 b로 가는 거리 c를 입력받아 그래프 작성
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 각 노드 k에 대해 a에서 b로 가는 최단거리 갱신
# a-b로 직접가는 것보다 a-k-b로 가는 거리가 짧으면 갱신
for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 출력
for a in range(1, V+1):
    for b in range(1, V+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
