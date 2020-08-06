import sys

sys.stdin = open("D2_4836_input.txt", "r")


def color(r1, c1, r2, c2, col):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if paper[i][j] != 0:
                paper[i][j] += col
            else:
                paper[i][j] = col


def check():
    cnt = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                cnt += 1
    return cnt


t = int(input())

for test in range(t):
    n = int(input())
    paper = [[0]*10 for _ in range(10)]
    for i in range(n):
        r1, c1, r2, c2, col = map(int, input().split())
        color(r1, c1, r2, c2, col)
    print('#' + str(test + 1), check())
