import sys

sys.stdin = open("D2_1954_input.txt", "r")

def snare(num):
    matrix = [[0]*num for _ in range(num)]
    
    # 벽에 부딪힐 때마다 case를 바꿔줌
    # case가 바뀌면 우,하,좌,상 순으로 움직임
    case = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = 0
    y = 0    
 
    for i in range(1, num**2+1):
        matrix[x][y] = i
        next_x = x + dx[case%4]
        next_y = y + dy[case%4]
        
        
        # if next_x not in (0, num) or next_y not in (0, num) or matrix[next_x][next_y] != 0 :
        #     case += 1        


        if 0<= next_x < num and 0<= next_y < num and matrix[next_x][next_y] == 0 :
            pass
        else:
            case += 1
        
        # x와 y의 위치를 바꿔주고 종료
        x += dx[case%4]
        y += dy[case%4]

    for v in matrix:
        print(' '.join(map(str, v)))
        
t = int(input())

for test in range(t):
    n = int(input())    
    print('#'+str(test+1))
    snare(n)