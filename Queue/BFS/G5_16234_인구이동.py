from collections import deque

# 인구이동이 일어나야할 곳을 체크하고 이동을 진행
def bfs_check(v):
    global temp
    q = deque([v])          # bfs에 사용할 덱
    q_cal = deque()      # 인구 계산에 사용할 덱
    trans_list[v[0]][v[1]] = 1
    size = 1
    population = pop_list[v[0]][v[1]]
    while q:
        t = q.popleft()
        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]
            # 땅의 범위 안에 있어야 하고, 인구 이동 조건을 만족하며
            if 0 <= nx < n and 0 <= ny < n and l <= abs(pop_list[t[0]][t[1]]-pop_list[nx][ny]) <= r:
                # 이미 계산하지 않은 경우에 대해 추가함
                if not trans_list[nx][ny]:
                    q.append([nx, ny])
                    q_cal.append([nx, ny])
                    trans_list[nx][ny] = 1
                    size += 1
                    population += pop_list[nx][ny]
    # 반복문을 다 돌았으면 인구이동이 일어날 곳은 다 체크한 것
    # 이제 계산 실시
    if q_cal:
        temp += 1
        q_cal.append(v)
        pop = population // size
        while q_cal:
            w = q_cal.popleft()
            pop_list[w[0]][w[1]] = pop
        

n, l, r = map(int, input().split())
pop_list = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
temp = 0
while True:
    # visit과 비슷한데, 인구이동이 일어날 곳을 저장함
    trans_list = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 인구이동 리스트에 없으면 이동해야하는지 체크
            if not trans_list[i][j]:
                bfs_check([i, j])

    # 인구이동이 일어나지 않았으면 끝났으므로 break
    if temp == result:
        break
        
    result += 1
    temp = result
    
print(result)