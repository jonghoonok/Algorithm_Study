import sys

sys.stdin = open("D3_1217_input.txt", "r")

for test_case in range(10):
    t = int(input())
    n, m = map(int, input().split())
    print('#' + str(test_case + 1), n**m)