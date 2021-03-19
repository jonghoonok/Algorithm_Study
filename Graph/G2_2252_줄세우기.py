from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for node in graph[now]:
        indegree[node] -= 1
        if not indegree[node]:
            q.append(node)

print(' '.join(map(str, result)))