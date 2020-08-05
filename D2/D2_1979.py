import sys

sys.stdin = open("D2_1979_input.txt", "r")

t = int(input())

def check(matrix):
    result = 0
    # 가로 방향 체크
    for i in range(n):        
        cnt = 0
        for j in range(n):            
            if matrix[i][j]: cnt +=1
            else:
                if cnt: 
                    if cnt == k: 
                        result += 1
                    cnt = 0
        if cnt == k: result +=1
            
    # 세로 방향 체크
    for i in range(n):
        cnt = 0
        for j in range(n):
            if matrix[j][i]: cnt +=1
            else:
                if cnt: 
                    if cnt == k: 
                        result += 1
                    cnt = 0
        if cnt == k: result +=1
    
    return result

for test in range(t):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    print('#'+str(test+1), check(puzzle))