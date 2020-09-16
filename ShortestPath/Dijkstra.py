# O(V^2)의 복잡도를 갖는 기본 알고리즘
def get_smallest_node():
    temp = INF
    index = 0
    for i in range(v+1):
        if distance[i] < temp and not visit[i]:
            temp = distance[i]
            index = i
    return index


def dijkstra(start):
    visit[start] = 1
    distance[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for i in range(v-1):
        now = get_smallest_node()
        visit[now] = 1
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
visit = [0]*(v+1)
distance = [INF]*(v+1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])