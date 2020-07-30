import sys

sys.stdin = open("D3_1209_input.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += matrix[i][j]
        if temp > result: result = temp
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += matrix[j][i]
        if temp > result: result = temp
    
    temp = 0
    for i in range(100):
        temp += matrix[i][i]
    if temp > result: result = temp
    temp = 0
    for i in range(100):
        temp += matrix[i][99-i]
    if temp > result: result = temp
    
    print('#'+str(test_case), result)