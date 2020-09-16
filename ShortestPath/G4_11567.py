INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

flag = True
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] < 0:
            flag = False
if flag:
    for i in range(2, n+1):
        if graph[1][i] == INF:
            print(-1)
        else:
            print(graph[1][i])
else:
    print(-1)