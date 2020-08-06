import sys

sys.stdin = open("D2_1961_input.txt", "r")


def rotate(numbers):
    numbers_90 = []
    numbers_180 = []
    numbers_270 = []

    for i in range(n):
        element = ''
        for j in range(n-1, -1, -1):
            element += str(numbers[j][i])
        numbers_90.append(element)

    for i in range(n-1, -1, -1):
        element = ''
        for j in range(n-1, -1, -1):
            element += str(numbers[i][j])
        numbers_180.append(element)

    for i in range(n-1, -1, -1):
        element = ''
        for j in range(n):
            element += str(numbers[j][i])
        numbers_270.append(element)

    for i in range(n):
        print(numbers_90[i], end=' ')
        print(numbers_180[i], end=' ')
        print(numbers_270[i], end=' ')
        print()


t = int(input())

for test_case in range(t):
    n = int(input())
    numList = [list(map(int, input().split())) for _ in range(n)]
    print('#'+str(test_case+1))
    rotate(numList)
