import sys

sys.stdin = open("D3_1206_input.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    apart_list = list(map(int, input().split()))
    check_list = [[0 for _ in range(255)] for _ in range(n)]    
    
    for i in range(n):
        for j in range(apart_list[i]):
            check_list[i][j] = 1
    
    result = 0
    for i in range(2, n-2):
        for j in range(apart_list[i]):            
            if check_list[i-2][j]==check_list[i-1][j]==check_list[i+1][j]==check_list[i+2][j]==0:
                result +=1

    print('#'+str(test_case), result)