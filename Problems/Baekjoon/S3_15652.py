# 백준 15652번
# N과 M(4)

import sys

sys.stdin = open("S3_15652_input.txt", "r")


def N_M_4(index, post):
    if index == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(post, N+1):
        arr[index] = i
        N_M_4(index+1, i)


for i in range(3):
    N, M = map(int, input().split())
    print('#'+str(i+1))
    arr = [0]*M
    N_M_4(0, 1)