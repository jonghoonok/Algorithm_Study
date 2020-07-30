import sys

sys.stdin = open("D2_2001_input.txt", "r")

t = int(input())

def paris(n, m, matrix):
    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for k in range(m):
                for l in range(m):                
                    temp += matrix[i+k][j+l]
                    if temp > result: result = temp
    return result

for test_case in range(t):
    n, m = map(int, input().split())    
    parisMatrix = [list(map(int, input().split())) for _ in range(n)]
    print('#'+str(test_case+1), paris(n, m, parisMatrix))