import sys

sys.stdin = open("D3_1217_input.txt", "r")

# 1: N, 2: S
def magnet():
    for i in range(100):
        column = []
        for j in range(100):
            column.append(table[j][i])
        # 각 column의 왼쪽이 N, 오른쪽이 S극이 위치하게 됨

        # 자성체의 갯수에 따라서 발생하는 상황 정리해보고 풀 것
        for k in range(100):
            if column[k] ==
    return result


for test_case in range(10):
    t = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    print('#' + str(test_case + 1), magnet())
