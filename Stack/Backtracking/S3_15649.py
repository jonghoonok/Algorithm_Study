# 백준 15649번
# N과 M(1)

import sys

sys.stdin = open("S3_15649_input.txt", "r")


def N_M_1(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        if check[i]:
            continue
        arr[index] = i
        check[i] = True
        N_M_1(index+1)
        check[i] = False


for i in range(3):
    N, M = map(int, input().split())
    print('#'+str(i+1))
    arr = [0]*M
    check = [0]*(N+1)
    N_M_1(0)