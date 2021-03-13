def dfs(x, y):
    index = ord(arr[x][y]) - 65
    visit[index] = 1

    # 현재 위치에서 말단 node까지 '자신을 포함한' 거리
    dist = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        temp = 0
        if 0 <= nx < r and 0 <= ny < c and not visit[ord(arr[nx][ny]) - 65]:
            temp = 1 + dfs(nx, ny)
            if temp > dist:
                dist = temp
    
    # 갈 수 있는 4방향 중에서 가장 멀리까지 갈 수 있는 거리를 리턴
    # 갈 수 있는 곳이 없으면 자기 자신만을 포함한 1을 리턴
    visit[index] = 0
    return dist

r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input()))

# 알파벳을 visit에 append하고 pop하는 방식은 느리기 때문에 ord를 이용하는 것으로 시간 단축
visit = [0]*26
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(dfs(0, 0))