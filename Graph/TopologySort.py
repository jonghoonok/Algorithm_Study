# 방향 그래프의 모든 노드를 방향성에 어긋나지 않게 나열
# 예) 선수과목을 고려한 학습 설정
# O(V+E)
from collections import deque


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(now)

    print(' '.join(result))


v, e = map(int, input().split())
# 진입차수: 해당 노드로 들어오는 간선의 갯수
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()
