import sys

sys.stdin = open("D2_4869_input.txt", "r")


# 그냥 재귀: 시간복잡도 매우 높음
def paper(width):    
    if width == 10:
        return 1
    elif width == 20:
        return 3
    else:
        return paper(width-10)+paper(width-20)*2


# memoization을 활용한 재귀
def paper2(width):       
    if memoization[width] != 0:
        return  memoization[width]
    else:
        memoization[width] = paper2(width-10) + paper2(width-20)*2
    return memoization[width]


# 반복문
def paper3(width):
    for i in range(30, n+10, 10):
        memoization[i] = memoization[i-10] + memoization[i-20]*2
    return memoization[width]


t = int(input())
for test in range(t):
    n = int(input())
    memoization = [0]*(n+1)
    memoization[10] = 1
    memoization[20] = 3
    print('#'+str(test+1), paper3(n))