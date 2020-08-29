import sys

sys.stdin = open("D3_1491_input.txt", "r")


def wall(n, a, b):
    r = n
    c = 1
    result = a*(r-c) + b*(n-r*c)
    while r >0:
        while r*c <= n and c <= r:
            temp = a*(r-c) + b*(n-r*c)
            if result > temp:
                result = temp
            c += 1
        r -= 1
        c = 1
    return result

t = int(input())
for test_case in range(t):
    n, a, b = map(int, input().split())   
    print('#' + str(test_case + 1), wall(n, a, b))
