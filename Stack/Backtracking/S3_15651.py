# 백준 15651번
# N과 M(3)

import sys

sys.stdin = open("S3_15651_input.txt", "r")


def N_M_3(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        arr[index] = i
        N_M_3(index+1)


for i in range(3):
    N, M = map(int, input().split())
    print('#'+str(i+1))
    arr = [0]*M
    N_M_3(0)