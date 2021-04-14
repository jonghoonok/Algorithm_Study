from collections import deque

# BFS로 풀이
def numIslands_1(grid):
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                bfs(i, j)
                result += 1
    return result


# DFS로 풀이
def numIslands_2(grid):
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                result += 1
    return result


# 중첩함수를 이용해 코드를 간결하게
def numIslands_3(self, grid: List[List[str]]) -> int:
    def dfs(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'

        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
    
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                result += 1
    return result



def dfs(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
        return
    grid[x][y] = '0'

    dfs(grid, x-1, y)
    dfs(grid, x, y+1)
    dfs(grid, x+1, y)
    dfs(grid, x, y-1)


def bfs(grid, x, y):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    q = deque()
    
    visited[x][y] = True
    q.append((x, y))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        t = q.popleft()
        grid[t[0]][t[1]] = '0'
        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]
            if 0<= nx < len(grid) and 0<= ny < len(grid[0]) and grid[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands_1(grid))