from collections import deque

def ice_maker():
    result = 0
    for i in range(N):
        for j in range(M):
            if not ice[i][j]:
                bfs([i, j])
                result += 1

    return result

def bfs(v):    
    # deque([start]) start를 꼭 []로 감싸줘야함....
    queue = deque([v])
    ice[v[0]][v[1]] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        t = queue.popleft()
        nx = t[0]    
        ny = t[1]
        for i in range(4):
            if 0 <= nx < N and 0 <= ny < M and not ice[nx][ny]:
                queue.append([nx, ny])
                ice[nx][ny] = 1
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]


N, M = map(int, input().split())
ice = [list(map(int, input())) for _ in range(N)]
print(ice_maker())