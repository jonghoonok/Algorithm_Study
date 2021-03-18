import heapq


n, m = map(int, input().split())
maze = []
for _ in range(m):
    maze.append(list(map(int, input())))

# 0에서 0으로 이동하는 거리: 0
# 0에서 1로 이동하는 거리: 1
INF = n*m
dist = [[INF]*n for _ in range(m)]

# 출발점의 거리는 0
dist[0][0] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dijkstra = []

# 다익스트라: 0과 인접한 노드들의 거리를 업데이트
heapq.heappush(dijkstra, (0, (0, 0)))
while dijkstra:
    d, now = heapq.heappop(dijkstra)
    if dist[now[0]][now[1]] < d:
        continue
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0<=nx<m and 0<=ny<n:
            # 인접한 노드가 0이면 now의 d값을 그대로 가져감
            if not maze[nx][ny]:
                cost = d
            # 인접한 노드가 1이면 now의 d값에 1을 더한 값을 거리로 함
            else:
                cost = d+1
            # 인접한 노드의 최단거리를 업데이트할 수 있으면 우선순위 큐에 넣어줌
            if cost < dist[nx][ny]:
                dist[nx][ny] = cost
                heapq.heappush(dijkstra, (cost, (nx, ny))) 

print(dist[m-1][n-1])