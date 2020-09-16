from collections import deque
import sys


def bfs(v):
    q = deque([v])
    visit[v] = 0
    while q:
        t = q.popleft()
        if visit[t] == k:
            break
        for w in graph[t]:
            if visit[w] == -1:
                q.append(w)
                visit[w] = visit[t] + 1


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visit = [-1]*(n+1)

bfs(x)

if k not in visit:
    print(-1)
else:
    for i in range(len(visit)):
        if visit[i] == k:
            print(i)