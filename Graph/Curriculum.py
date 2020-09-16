from collections import deque
import copy


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for node in graph[now]:
            result[node] = max(result[max], result[now]+time[node])
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)
    
    for i in range(1, n+1):
        print(result[i])


n = int(input())
time = [0]*(n+1)
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]
        graph[i].append(i)

topology_sort()