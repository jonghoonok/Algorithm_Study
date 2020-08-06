import sys

sys.stdin = open("D3_4837_input.txt", "r")

def powersum(num, p_sum):
    cnt = 0

    # bit mask를 이용해 부분집합 탐색
    for i in range(1 << 12):
        cnt_num = 0     # 부분집합 원소가 5개인지 체크하는 데 사용
        result = 0      # 원소의 합이 k와 일치하는지 확인에 사용
        for j in range(12):
            if i & 1 << j:
                cnt_num += 1
                result += j+1
        if cnt_num == num:
            if result == p_sum:
                cnt += 1

    return cnt


t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    print('#' + str(test_case), powersum(n, k))
