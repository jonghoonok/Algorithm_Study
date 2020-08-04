import sys

sys.stdin = open("D3_1206_input.txt", "r")

# 풀이 1: 2중 for문을 이용한 행렬 내 완전탐색
'''
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
'''

# 풀이 2: for문 하나만 사용하여 O(N)으로 풀 수 있음
for test_case in range(1, 11):
    n = int(input())
    apart_list = list(map(int, input().split()))
    
    result = 0
    for i in range(2, n-2):
        # 양옆 2개 아파트보다 낮으면 pass, 높으면 조망이 확보되는 만큼 count        
        # max_for_i = max(apart_list[i-2], apart_list[i-1], apart_list[i+1], apart_list[i+2])

        max_for_i = apart_list[i-2]
        if apart_list[i-1] > max_for_i: max_for_i = apart_list[i-1]
        if apart_list[i+1] > max_for_i: max_for_i = apart_list[i+1]
        if apart_list[i+2] > max_for_i: max_for_i = apart_list[i+2]
        # max 쓰지 말라고 하셔서..

        if apart_list[i] <= max_for_i:
            continue
        else:
            result += apart_list[i] - max_for_i
    print('#'+str(test_case), result)