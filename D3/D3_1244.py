import sys

sys.stdin = open("D3_1244_input.txt", "r")


def change(num, cnt):
    


t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())   
    print('#' + str(test_case + 1), change(n, m))
