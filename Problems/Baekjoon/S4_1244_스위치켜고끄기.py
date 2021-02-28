def change_switch(index):
    if switches[index] == 1:
        switches[index] = 0
    else:
        switches[index] = 1


n_switch = int(input())
switches = list(map(int, input().split()))
n_student = int(input())
for _ in range(n_student):
    sex, num = map(int, input().split())
    if sex == 1:
        # 남자
        for i in range(n_switch):
            if (i+1) % num != 0:
                continue
            else:
                change_switch(i)
    else:
        # 여자
        j = 1
        while(num-1 - j >= 0 and num-1 + j < n_switch):
            if switches[num-1-j] != switches[num-1+j]:
                break
            j += 1
        j -= 1  # 스위치의 상태가 같지 않은 시점에서 j가 종료되었기 때문에 1을 빼주어야 함

        for i in range(num-1-j, num-1+j+1):
            change_switch(i)


for i in range(n_switch):
    if (i+1) % 20 == 0:
        print(switches[i])
    else:
        print(switches[i], end=" ")