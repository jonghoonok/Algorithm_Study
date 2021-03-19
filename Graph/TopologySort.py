from collections import deque


v, e = map(int, input().split())
# 진입차수: 해당 노드로 들어오는 간선의 갯수
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()

for i in range(1, v+1):
    # 진입차수가 0인 노드를 큐에 넣는다
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for node in graph[now]:
        # 현재 방문중인 노드에서 출발하는 간선을 제거: 도착 노드들의 진입차수 -=1
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(now)

# 방문한 노드를 순서대로 출력
print(' '.join(result))