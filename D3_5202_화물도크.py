import sys

sys.stdin = open("D3_5202_화물도크_input.txt", "r")


def dock():
    # 가장 먼저 끝나는 작업의 끝나는 시각을 end에 저장
    end = trucks.pop()[1]
    answer = 1
    while trucks:
        s, e = trucks.pop()
        # 그다음으로 늦게 끝나는 작업의 시작시각이 end보다 늦으면 이 작업은 가능
        if s >= end:
            answer += 1
            end = e
        # 그렇지 않으면 처리 불가하니 다음으로 넘긴다
        else:
            continue
    return answer


t = int(input())
for test_case in range(t):
    n = int(input())
    trucks = [list(map(int, input().split())) for _ in range(n)]
    # 빨리 끝나는 순서대로 정렬함
    trucks.sort(key=lambda x:x[1], reverse=True)
    print('#' + str(test_case + 1), dock())