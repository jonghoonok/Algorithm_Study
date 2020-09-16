from collections import deque

def dummy():
    time = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    direction = 1
    
    head_x, head_y = 1, 1       # 머리의 위치 1행 1열
    body = deque()
    body.append((head_x, head_y))
    board[head_x][head_y] = 1
    
    snake = True        # 머리가 몸에 부딪히면 False
    while True:
        # 먼저 해당 시각에 입력된 커맨드대로 방향전환이 있는지 체크
        if command:
            if command[0][0] == time:
                if command[0][1] == 'L':
                    direction = (direction + 3) % 4                
                else:
                    direction = (direction + 1) % 4            
                command.popleft()     

        # 바라보고 있는 방향으로 몸을 늘려 머리를 위치시킴 
        head_x += dx[direction]
        head_y += dy[direction]
        if head_x < 1 or head_x > n or head_y < 1 or head_y > n:
            return time + 1
        if board[head_x][head_y] == 0:  # 사과가 없으면 꼬리 한 칸 제거, 있으면 pass
            tail_x, tail_y = body.popleft() 
            board[tail_x][tail_y] = 0
        board[head_x][head_y] = 1
        body.append((head_x, head_y))        

        # 머리가 몸에 부딪혔는지 check
        for i in range(0, len(body)-1):
            if body[i] == (head_x, head_y):
                snake = False                
                return time
                
        time += 1

n = int(input())
board = [[0]*(n+1) for _ in range(n+1)]

k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = 2

l = int(input())
command = deque()
for _ in range(l):
    x, c = input().split()
    command.append((int(x), c))

print(dummy())