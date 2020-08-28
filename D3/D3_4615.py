import sys

sys.stdin = open("D3_4615_input.txt", "r")


def plate_setting(n):
    plate[n//2-1][n//2-1] = 2
    plate[n//2][n//2] = 2
    plate[n//2-1][n//2] = 1
    plate[n//2][n//2-1] = 1

def check(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if not plate[y][x]:
        return False
    return True


def othello(x, y, color):
    x -= 1
    y -= 1
    plate[y][x] = color
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    if color == 1:
        for i in range(8):
            if check(x+dx[i], y+dy[i]):
                new_x = x+dx[i]
                new_y = y+dy[i]                
                while check(new_x, new_y) and plate[new_y][new_x] == 2:                    
                    new_x += dx[i]
                    new_y += dy[i]                    
                if check(new_x, new_y) and plate[new_y][new_x] == 1:
                    new_x -= dx[i]
                    new_y -= dy[i]
                    while plate[new_y][new_x] == 2:
                        plate[new_y][new_x] = 1
                        new_x -= dx[i]
                        new_y -= dy[i]                        
    else:
        for i in range(8):
            if check(x+dx[i], y+dy[i]):
                new_x = x+dx[i]
                new_y = y+dy[i]                
                while check(new_x, new_y) and plate[new_y][new_x] == 1:                    
                    new_x += dx[i]
                    new_y += dy[i]                    
                if check(new_x, new_y) and plate[new_y][new_x] == 2:
                    new_x -= dx[i]
                    new_y -= dy[i]
                    while plate[new_y][new_x] == 1:
                        plate[new_y][new_x] = 2
                        new_x -= dx[i]
                        new_y -= dy[i]


def game_result():
    cnt_b = 0
    cnt_w = 0
    for i in range(n):
        for j in range(n):
            if plate[i][j] == 1:
                cnt_b += 1
            elif plate[i][j] == 2:
                cnt_w += 1 
    return str(cnt_b)+' '+str(cnt_w)


t = int(input())
for test in range(t):
    n, m = map(int, input().split())
    plate = [[0]*n for _ in range(n)]
    plate_setting(n)
    for i in range(m):
        x, y, color = map(int, input().split())
        othello(x, y, color)
    print('#'+str(test+1), game_result())