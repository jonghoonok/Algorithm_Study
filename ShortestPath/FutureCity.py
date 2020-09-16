INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

X, K = map(int, input().split())
result = graph[1][K] + graph[K][X]
if result >= INF:
    print(-1)
else:
    print(result)