from itertools import combinations
from collections import deque
import copy


def laboratory():
    safe_max = 0    
    
    # 안전 구역 중 벽을 세울 3개를 뽑는 모든 조합
    coms = list(combinations(safe_list, 3))
    for com in coms:    
        # 각 조합에 대해 벽을 세움
        lab[com[0][0]][com[0][1]] = 1
        lab[com[1][0]][com[1][1]] = 1
        lab[com[2][0]][com[2][1]] = 1
        # 바이러스를 퍼뜨린 뒤 안전구역의 갯수 temp를 계산
        temp = virus_start()
        # 현재 최댓값과 비교해서 크면 갱신
        if temp > safe_max:
            safe_max = temp
        # lab을 원상복구한 뒤 다음 조합으로 넘겨 다시 계산                
        lab[com[0][0]][com[0][1]] = 0
        lab[com[1][0]][com[1][1]] = 0
        lab[com[2][0]][com[2][1]] = 0        
    
    return safe_max


def virus_start():
    virus_list = []
    wall_list = []
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                virus_list.append((i, j))
            elif lab[i][j] == 1:
                wall_list.append((i, j))
    
    # 모든 바이러스에 대해 bfs를 돌려서 오염된 lab을 얻음
    for virus in virus_list:
        bfs(virus)                
    
    # 안전구역의 수를 카운트하고 랩 원상복구하여 리턴
    safe_num = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:    
                safe_num += 1
            if (i, j) in safe_list:
                lab[i][j] = 0

    return safe_num          


def bfs(v):    
    q = deque([v])    
    while q:
        t = q.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        nx = t[0]
        ny = t[1]
        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                q.append((nx, ny))                
                lab[nx][ny] = 2


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
# lab의 안전구역을 저장하는 리스트
safe_list = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            safe_list.append((i, j))            

print(laboratory())