import sys

sys.stdin = open("D2_4839_input.txt", "r")


def binary_search(P, target):
    cnt = 0
    start = 1
    end   = P
    mid   = (start+end)//2

    while True:
        cnt += 1
        if mid == target:
            return cnt # 이진탐색이 수행된 횟수를 리턴
        else:
            if target < mid:
                end = mid
                mid = (start+end)//2
            else:
                start = mid
                mid = (start+end)//2

# 풀이 2: 재귀를 이용한 이진탐색
'''
def binary_search2(P, start, end, target):
    mid = (start + end)//2
    if mid == target:
        return 1
    else:
        if target < mid:
            return 1 + binary_search2(P, start, mid, target)
        else:
            return 1 + binary_search2(P, mid, end, target)
'''

def game(a, b):
    if a < b:
        return 'A'
    elif a > b:
        return 'B'
    else:
        return 0


t = int(input())

for test in range(t):
    P, Pa, Pb = map(int, input().split())
    print('#' + str(test + 1), game(binary_search(P, Pa), binary_search(P, Pb)))
