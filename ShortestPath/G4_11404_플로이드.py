import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
# 한 도시에서 다른 도시로 가는 최대한의 비용은 99*100000 이므로 INF를 10^7으로 설정
INF = 10000000
graph = [[INF]*n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0
    
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    if graph[a-1][b-1] > cost:
        graph[a-1][b-1] = cost

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0
    print(' '.join(map(str, graph[i])))