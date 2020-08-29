import sys

sys.stdin = open("D3_1493_input.txt", "r")


def cartesian(p, q):
    x1, y1 = findxy(p)
    x2, y2 = findxy(q)
    return findxy2(x1+x2, y1+y2)


def findxy(n):
    result = [0, 2]
    cnt = 0
    while cnt < n:
        if result[1] == 1:
            result[1] = result[0] + 1
            result[0] = 1
        else:
            result[0] += 1
            result[1] -= 1
        cnt += 1
    return result[0], result[1]

def findxy2(x, y):
    result = [0, 2]
    cnt = 0
    while result[0] != x or result[1] != y:
        if result[1] == 1:
            result[1] = result[0] + 1
            result[0] = 1
        else:
            result[0] += 1
            result[1] -= 1
        cnt += 1        
    return cnt

t = int(input())
for test_case in range(t):
    p, q = map(int, input().split())       
    print('#' + str(test_case + 1), cartesian(p, q))
