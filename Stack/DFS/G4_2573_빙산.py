import sys
# 최대 노드의 갯수 10**4이므로 recursionlimit도 같은 값으로 설정
sys.setrecursionlimit(10**4)


def melt():
    global ice
    # 빙산 주위 바닷물의 갯수를 저장하는 배열
    water = [[0]*m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if sea[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 지도의 가장자리는 항상 0이기 때문에 nx, ny가 범위를 벗어나는지 체크 불필요
                    # if 0 <= nx < n and 0 <= ny < m and not sea[nx][ny]:
                    if not sea[nx][ny]:
                        water[x][y] += 1
    
    # 바닷물의 갯수만큼 빙하를 녹임
    for x in range(n):
        for y in range(m):
            if sea[x][y]:
                sea[x][y] = 0 if water[x][y] > sea[x][y] else sea[x][y] - water[x][y]
            if sea[x][y]:
                ice += 1


def dfs(x, y):
    cnt = 1     # 연결된 빙산의 갯수
    visit[x][y] = 1
    stack = [(x, y)]

    while stack:
        t = stack.pop()
        x, y = t[0], t[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # if 0 <= nx < n and 0 <= ny < m and sea[nx][ny] and not visit[nx][ny]:
            # 지도의 가장자리는 항상 0이기 때문에 nx, ny가 범위를 벗어나는지 체크 불필요
            if sea[nx][ny] and not visit[nx][ny]:
                cnt += 1
                stack.append((nx, ny))
                visit[nx][ny] = 1
        # 현재 보고있는 덩어리가 빙산 전체 갯수와 같다면 더 이상 탐색이 불필요하므로 return
        if cnt == ice:
            return

n, m = map(int, input().split())
sea = []
for _ in range(n):
    sea.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

year = 1
while True:
    ice = 0     # 전체 빙하의 갯수
    melt()      # 빙하를 녹임

    # 분리됐는지 검사
    result = 0      # 분리된 갯수
    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if sea[i][j] and not visit[i][j]:
                result += 1
                if result > 1: break
                dfs(i, j)
        if result > 1: break

    # 갯수가 2개 이상이거나 다 녹았으면 종료
    if result != 1:
        if result == 0:
            print(0)
        else:
            print(year)
        break
    
    year += 1