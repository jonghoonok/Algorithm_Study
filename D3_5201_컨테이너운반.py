import sys

sys.stdin = open("D3_5201_컨테이너운반_input.txt", "r")


def transport():
    result = 0
    for truck in trucks:
        temp = 0    # 현재 트럭에 적재된 무게
        idx = 0
        for i in range(len(containers)):
            # 컨테이너의 무게가 현재무게보다 크고 적재용량보다 작으면 싣음
            if containers[i] > temp and containers[i] <= truck:
                temp = containers[i]
                idx = i
        if temp:
            result += temp        
            containers[idx] = 0
    return result


t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    print('#' + str(test_case + 1), transport())