from collections import deque

def bfs(v):
    q = deque([v])
    visit[v[0]][v[1]][1] = 1
    while q:
        x, y, drill = q.popleft()
        # 드릴로 뚫었건 안 뚫었건 빨리 목적지에 도달하면 최단경로이므로 리턴하고 종료
        if x == n-1 and y == m-1:
            return visit[x][y][drill]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 탐색할 곳이 지도를 벗어나지 않는가
            if 0 <= nx < n and 0 <= ny < m:
                # 경우1: nx, ny가 갈 수 있는 길임 - drill과는 무관
                if not maze[nx][ny] and not visit[nx][ny][drill]:
                    q.append((nx, ny, drill))
                    visit[nx][ny][drill] = visit[x][y][drill] + 1
                # 경우2: nx, ny는 벽이지만 뚫고 진행
                elif maze[nx][ny] and drill == 1:
                    # 드릴은 1번만 사용할 수 있으므로 0으로 값을 바꿔줌
                    q.append((nx, ny, 0))
                    visit[nx][ny][0] = visit[x][y][1] + 1
   
    # q를 다 돌았는데 return되지 않았다: 도달할 수 없음
    return -1

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# visit을 3차원 배열로 구성: x좌표, y좌표, 뚫을 수 있는지 여부(0: 이미 뚫은 상태, 1: 뚫을 수 있는 상태)
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
print(bfs((0, 0, 1)))