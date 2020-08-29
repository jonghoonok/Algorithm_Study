import sys

sys.stdin = open("D3_1873_input.txt", "r")


def game_result():
    i = 0
    location = [0, 0]       # 현재 전차가 있는 위치 x, y좌표 저장
    for i in range(h):
        for j in range(w):
            if game_map[i][j] in UDLR:
                location[0] = j
                location[1] = i
                break
    i = 0
    while i < n:
        if cmd[i] == 'U':
            game_map[location[1]][location[0]] = '^'
            if 0 <= location[0] < w and 0 <= location[1]-1 < h and game_map[location[1]-1][location[0]] == '.':
                game_map[location[1]-1][location[0]] = '^'
                game_map[location[1]][location[0]] = '.'
                location[1] -= 1
        elif cmd[i] == 'D':
            game_map[location[1]][location[0]] = 'v'
            if 0 <= location[0] < w and 0 <= location[1]+1 < h and game_map[location[1]+1][location[0]] == '.':
                game_map[location[1]+1][location[0]] = 'v'
                game_map[location[1]][location[0]] = '.'
                location[1] += 1
        elif cmd[i] == 'L':
            game_map[location[1]][location[0]] = '<'
            if 0 <= location[0]-1 < w and 0 <= location[1] < h and game_map[location[1]][location[0]-1] == '.':
                game_map[location[1]][location[0]-1] = '<'
                game_map[location[1]][location[0]] = '.'
                location[0] -= 1
        elif cmd[i] == 'R':
            game_map[location[1]][location[0]] = '>'
            if 0 <= location[0]+1 < w and 0 <= location[1] < h and game_map[location[1]][location[0]+1] == '.':
                game_map[location[1]][location[0]+1] = '>'
                game_map[location[1]][location[0]] = '.'
                location[0] += 1
        elif cmd[i] == 'S':
            shoot(location[0], location[1])
        i += 1

    for v in game_map:
        print(''.join(map(str, v)))


def shoot(x, y):    
    move = UDLR.index(game_map[y][x])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    new_x = x
    new_y = y
    while True:
        new_x += dx[move]
        new_y += dy[move]
        if new_x<0 or new_x>=w or new_y<0 or new_y>=h:
            break
        if game_map[new_y][new_x] == '*':
            game_map[new_y][new_x] = '.'
            break
        if game_map[new_y][new_x] == '#':
            break

t = int(input())
for test_case in range(t):
    h, w = map(int, input().split())
    game_map = [list(input()) for _ in range(h)]
    n = int(input())
    cmd = input()
    UDLR = ['^', 'v', '<', '>']
    print('#' + str(test_case + 1), end = ' ')    
    game_result()
