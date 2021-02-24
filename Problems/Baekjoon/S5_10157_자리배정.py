c, r = map(int, input().split())
k = int(input())

if k > c*r:
    print(0)
else:
    arr = [[0]*r for _ in range(c)]
    cnt, x, y = 1, 0, -1
    dir = 0 # 방향을 나타내는 변수, 0: 우, 1: 하, 2: 좌, 3: 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while(cnt <= k):
        x += dx[dir]
        y += dy[dir]

        # 처음 한 바퀴를 제외하면 나가는 일은 없으니 튜닝을 해주는 것이 좋음
        # if (i<0 or i>=c or j<0 or j>=r or arr[i][j] != 0):
        if cnt > 2 * (r + c) - 4:
            if arr[x][y] != 0:
                x -= dx[dir]
                y -= dy[dir]
                dir = (dir + 1) % 4
                x += dx[dir]
                y += dy[dir]
        else:
            if (x<0 or x>=c or y<0 or y>=r):
                x -= dx[dir]
                y -= dy[dir]
                dir = (dir + 1) % 4
                x += dx[dir]
                y += dy[dir]

        arr[x][y] = cnt
        cnt += 1

    print(x+1, y+1)