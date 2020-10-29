import sys

sys.stdin = open("D3_5188_최소합_input.txt", "r")


# 재귀적으로 구현
def min_sum(cursum, i, j):
    # 오른쪽 아래에 도달하면 리턴
    if i == j == n-1:
        return cursum
    # 제일 아랫줄에 도달하면 오른쪽으로만 이동
    if i == n-1:
        return min_sum(cursum + num_list[i][j+1], i, j+1)
    # 제일 오른쪽줄에 도달하면 아랫쪽으로만 이동
    if j == n-1:
        return min_sum(cursum + num_list[i+1][j], i+1, j)

    # 오른쪽으로 이동할 경우의 합
    right = min_sum(cursum + num_list[i][j+1], i, j+1)
    # 아랫쪽으로 이동할 경우의 합
    down = min_sum(cursum + num_list[i+1][j], i+1, j)
    
    # 둘 중 작은 값을 리턴
    if right < down:
        return right
    else:
        return down


t = int(input())
for test_case in range(t):
    n = int(input())
    num_list = [list(map(int, input().split())) for _ in range(n)]
    print('#' + str(test_case + 1), min_sum(num_list[0][0], 0, 0))