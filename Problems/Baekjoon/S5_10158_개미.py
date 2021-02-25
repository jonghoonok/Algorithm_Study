# 조건문을 이용하여 한번씩 이동
# 하면 시간 제한에 걸리니까 벽에 부딪히는 경우만 계산
def ant_1():
    dir = 0      # 0: 우상, 1: 좌상, 2: 좌하, 3: 우하
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]

    while(t > 0):
        if dir == 0:
            # 우측 벽 거리 계산
            dist_right = w-x
            # 상측 벽 거리 계산
            dist_up = h-y
            if dist_right > dist_up:
                # 위로 감
                if t > dist_up:
                    x += dx[dir] * dist_up
                    y += dy[dir] * dist_up
                    t -= dist_up
                    dir = 3
                else:
                    x += dx[dir] * t
                    y += dy[dir] * t
                    t -= t

            else:
                # 오른쪽으로 감
                if t > dist_up:
                    x += dx[dir] * dist_right
                    y += dy[dir] * dist_right
                    t -= dist_right
                    dir = 1
                else:
                    x += dx[dir] * t
                    y += dy[dir] * t
                    t -= t
        elif dir == 1:
            # 좌측 벽 거리 계산
            dist_left = x
            # 상측 벽 거리 계산
            dist_up = h-y
            if dist_left > dist_up:
                # 위로 감
                if t > dist_up:
                    x += dx[dir] * dist_up
                    y += dy[dir] * dist_up
                    t -= dist_up
                    dir = 2
                else:
                    x += dx[dir] * t
                    y += dy[dir] * t
                    t -= t
            else:
                # 왼쪽으로 감
                if t > dist_left:
                    x += dx[dir] * dist_left
                    y += dy[dir] * dist_left
                    t -= dist_left
                    dir = 1
                else:
                    x += dx[dir] * t
                    y += dy[dir] * t
                    t -= t
        elif dir == 2:
            # 좌측 벽 거리 계산
            dist_left = x
            # 하측 벽 거리 계산
            dist_down = y
            if dist_left > dist_down:
                # 아래로 감
                if t > dist_down:
                    x += dx[dir] * dist_down
                    y += dy[dir] * dist_down
                    t -= dist_down
                    dir = 1
                else:
                    x += dx[dir] * t
                    y += dy[dir] * t
                    t -= t
            else:
                # 왼쪽으로 감
                if t > dist_left:
                    x += dx[dir] * dist_left
                    y += dy[dir] * dist_left
                    t -= dist_left
                    dir = 3
                else:
                    x += dx[dir] * t
                    y += dy[dir] * t
                    t -= t
        else:
            # 우측 벽 거리 계산
            dist_right = w-x
            # 하측 벽 거리 계산
            dist_down = y
            if dist_right > dist_down:
                # 아래로 감
                if t > dist_down:
                    x += dx[dir] * dist_down
                    y += dy[dir] * dist_down
                    t -= dist_down
                    dir = 0
                else:
                    x += dx[dir] * t
                    y += dy[dir] * t
                    t -= t
            else:
                # 오른쪽으로 감
                if t > dist_right:
                    x += dx[dir] * dist_right
                    y += dy[dir] * dist_right
                    t -= dist_right
                    dir = 2
                else:
                    x += dx[dir] * t
                    y += dy[dir] * t
                    t -= t

    # 모서리에 박히면?
    print(x, y)

# ant_1도 시간제한에 걸리기 때문에 수학적으로 해결
def ant_2(x, y):
    x += t
    y += t
    # 세로벽에 짝수번 부딪히면 인덱스가 같고, 홀수번 부딪히면 가로길이에서 x인덱스를 빼줘야 함
    if (x // w) % 2 == 0:
        x = x % w
    else:
        x = w - (x % w)
        
    # 가로벽에 짝수번 부딪히면 인덱스가 같고, 홀수번 부딪히면 세로길이에서 y인덱스를 빼줘야 함
    if (y // h) % 2 == 0:
        y = y % h
    else:
        y = h - (y % h)

    print(x, y)

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x, y = p, q

# ant_1()
ant_2(x, y)