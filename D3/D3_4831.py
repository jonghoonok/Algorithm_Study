import sys

sys.stdin = open("D3_4831_input.txt", "r")

def charge(num, busEnd, busStopList):
    energy = num
    num_of_charge = 0
    busStopList.insert(0, 0)
    busStopList.append(busEnd)
    for i in range(1, len(busStopList)-1):
        # 정류장 사이의 거리만큼 에너지 차감
        energy -= busStopList[i] - busStopList[i-1]
        
        # 에너지가 부족하면 0을 리턴
        if energy < 0 : return 0
        
        # 다음 정류장까지의 거리를 보고 에너지가 부족하면 충전
        if energy < busStopList[i+1] - busStopList[i]:
            num_of_charge += 1
            energy = num
    return num_of_charge

t = int(input())

for test_case in range(t):
    k, n, m = map(int, input().split())
    stopList = list(map(int, input().split()))    
    print('#'+str(test_case+1), charge(k, n, stopList))