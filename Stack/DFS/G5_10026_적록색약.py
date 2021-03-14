import sys
# 최대 영역의 갯수 100*100 = 10**4이므로 recursionlimit도 같은 값으로 설정
sys.setrecursionlimit(10**4)

def dfs(arr, x, y):
    color = arr[x][y]
    arr[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == color:
            dfs(arr, nx, ny)


n = int(input())
nonweak_pic = []
weak_pic = [[0]*n for _ in range(n)]
for _ in range(n):
    nonweak_pic.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 적록색약이 아닌 사람이 본 구역 수
non_weak = 0
# 적록색약이 아닌 사람이 본 구역 수
weak = 0
# 색약 환자가 보는 그림: 녹색을 다 빨간색으로 바꿈
for i in range(n):
    for j in range(n):
        # deepcopy를 쓸 수도 있지만 어차피 색깔 바꿔야해서 반복문으로 처리
        weak_pic[i][j] = nonweak_pic[i][j]
        if weak_pic[i][j] == 'G':
            weak_pic[i][j] = 'R'

# 색약 아닌 사람이 본 구역 수 계산
for i in range(n):
    for j in range(n):
        if nonweak_pic[i][j]:
            non_weak += 1
            dfs(nonweak_pic, i, j)

# 색약인 사람이 본 구역 수 계산
for i in range(n):
    for j in range(n):
        if weak_pic[i][j]:
            weak += 1
            dfs(weak_pic, i, j)

print(non_weak, weak)