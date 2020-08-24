import sys

sys.stdin = open("D3_1225_input.txt", "r")


def crypto(numbers):
    cnt = 1
    while True:
        num = numbers.pop(0) - cnt
        if num > 0:
            numbers.append(num)
        else:
            numbers.append(0)
            break
        cnt += 1
        if cnt > 5:
            cnt = 1        

    print(*numbers)


for test_case in range(10):
    n = int(input())
    numbers = list(map(int, input().split()))
    print('#' + str(test_case + 1), end=' ')
    crypto(numbers)
