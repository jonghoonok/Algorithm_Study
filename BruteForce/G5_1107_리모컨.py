# 모든 숫자를 1번씩 선택해가며 최소값을 구하기
def remote(num):
    global min_cnt, num_int, btn_set

    for btn in btn_set:
        temp = num + str(btn)
        min_cnt = min(min_cnt, abs(n - int(temp)) + len(temp))

        if len(temp) < 6:
            remote(temp)


min_cnt = int(1e9)
btn_set = {i for i in range(10)}    # 사용 가능한 숫자 버튼

n = int(input())
m = int(input())
min_cnt = min(min_cnt, abs(100 - n))

# m!=0 일때만 readline을 받기
btn_set -= set(map(int, input().split())) if m else set()

remote('')
print(min_cnt)