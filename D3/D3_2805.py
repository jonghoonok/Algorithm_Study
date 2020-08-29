import sys

sys.stdin = open("D3_2805_input.txt", "r")


def harvest():    
    result = 0
    for i in range(n):
        if i < n // 2:
            for j in range(n):
                if j < n // 2 - i:
                    continue
                elif j > n // 2 + i:
                    continue
                else:
                    result += farm[i][j]
        elif i == n // 2:
            for j in range(n):
                result += farm[i][j]
        else:
            for j in range(n):
                if j < n // 2 - n + i + 1:
                    continue
                elif j > n // 2 + n - i - 1:
                    continue
                else:
                    result += farm[i][j]
    return result

t = int(input())
for test_case in range(t):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    print('#' + str(test_case + 1), harvest())    
