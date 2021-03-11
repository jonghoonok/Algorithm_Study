import sys
sys.setrecursionlimit(10**6)
# DFS니까 일단 재귀로 풀어봤다

def dfs(x, y):
    arr[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < m and 0 <= ny < n and arr[nx][ny]:
            dfs(nx, ny)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
    
    result = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j]:
                result += 1
                dfs(i, j)
    
    print(result)
