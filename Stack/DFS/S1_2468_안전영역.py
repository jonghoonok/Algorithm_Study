import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and area[nx][ny] and not visit[nx][ny]:
            dfs(nx, ny)


n = int(input())
area = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    area.append(list(map(int, input().split())))

result = 0

# 내리는 비의 양에 따라서(~100) 안전한 영역의 갯수 구하기
for _ in range(100):
    visit = [[0]*n for _ in range(n)]

    # 안전한 영역의 갯수
    temp = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] and not visit[i][j]:
                temp += 1
                dfs(i, j)
    
    if temp > result:
        result = temp
    
    # 모든 지역이 침수되면 종료
    if temp == 0:
        break

    # 비가 온 만큼 높이를 깎음
    # 높이가 0이 되면 물에 잠긴 지역으로 계산
    for i in range(n):
        for j in range(n):
            if area[i][j]:
                area[i][j] -= 1

print(result)