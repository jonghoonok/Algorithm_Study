from collections import deque

def maze():
    visit = {}
    queue = deque([(1, 1)])
    visit[(1, 1)] = 1
    while queue:
        t = queue.popleft()
        if t == (N, M):
            return visit[t]
        
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        nx = t[0]
        ny = t[1]
        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]   
            if 1 <= nx <= N and 1 <= ny <= M and not visit.get((nx, ny)):
                queue.append((nx, ny))
                visit[(nx, ny)] = visit[t] + 1


N, M = map(int, input().split())
ice = [list(map(int, input())) for _ in range(N)]
print(maze())