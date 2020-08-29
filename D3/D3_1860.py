import sys

sys.stdin = open("D3_1860_input.txt", "r")


def boong(n, m, k): 
    stock = 0       # 붕어빵 재고
    cnt = 0         # 방문한 손님 수
    time = 0        # 경과 시간
    while time <= arrival[-1]:
        if time and time % m == 0:
            stock += k
        if time == arrival[cnt]:
            num = count(cnt)    # 동시에 방문한 손님 수
            if stock >= num:
                stock -= num
                cnt += num
            else:
                return 'Impossible'
        time += 1
    return 'Possible'


def count(index):
    cnt = 1
    if index == n-1:
        pass
    else:
        j = index
        while j < n-1:
            if arrival[j] == arrival[j+1]:
                cnt += 1
            else:
                break        
            j += 1
    return cnt


t = int(input())
for test_case in range(t):
    n, m, k = map(int, input().split())       
    arrival = sorted(list(map(int, input().split())))
    print('#' + str(test_case + 1), boong(n, m, k))
