from collections import deque
import sys

n = int(sys.stdin.readline())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

# 부모 노드를 담을 배열
parents = [0]*(n+1)

# 1번 노드부터 BFS를 돌면서 parents를 채운다
q = deque([1])
while q:
    node = q.popleft()
    for child in edges[node]:
        # 부모가 아직 기입되지 않은 경우에만 추가
        if not parents[child]:
            parents[child] = node
            q.append(child)

# 2번 노드부터 부모 노드를 출력
for i in range(2, n+1):
    print(parents[i])