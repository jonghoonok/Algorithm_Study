import sys

sys.stdin = open("D3_1217_input.txt", "r")

# 재귀호출을 이용하여 구현할 것
for test_case in range(10):
    t = int(input())
    n, m = map(int, input().split())
    print('#' + str(test_case + 1), n**m)