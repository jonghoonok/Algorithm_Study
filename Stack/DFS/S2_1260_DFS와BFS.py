import sys
from collections import deque

def dfs(v):
    stack = [v]
    visit = []
    while stack:
        t = stack.pop()
        if t not in visit:
            visit.append(t)
            edges[t].sort(reverse=True)
            for node in edges[t]:
                stack.append(node)

    print(' '.join(map(str, visit)))


def bfs(v):
    q = deque([v])
    visit = []
    while q:
        t = q.popleft()
        if t not in visit:
            visit.append(t)
            edges[t].sort()
            for node in edges[t]:
                q.append(node)

    print(' '.join(map(str, visit)))


n, m, v = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    edges[start].append(end)
    edges[end].append(start)

dfs(v)
bfs(v)