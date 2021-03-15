from collections import deque

def bfs(v):
    q = deque([v])
    visit[v[0]][v[1]] = 1
    while q:
        t = q.popleft()
        x, y = t[0], t[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] and not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1


n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [[0]*m for _ in range(n)]
bfs((0, 0))
print(visit[n-1][m-1])