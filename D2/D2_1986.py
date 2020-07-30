import sys

sys.stdin = open("D2_1986_input.txt", "r")

t = int(input())

for i in range(t):
    n = int(input())
    result = 0
    for j in range(1, n+1):
        if j % 2 == 0:
            result -= j
        else: result += j

    print('#'+str(i+1), result)