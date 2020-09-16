from itertools import combinations
import copy

def chicken():
    dist = int(1e9)
    num = 0             # 치킨집의 수
    chicken_list = []   # 치킨집 리스트
    for i in range(n):
        for j in range(n):
            if city[i][j] == 2:
                chicken_list.append((i, j))
                num += 1

    if num == m:
        dist = chicken_dist(city)
    else:
        # num C m 만큼의 경우의 수에 대해 따져야 함
        coms = list(combinations(chicken_list, m))
        new_city = copy.deepcopy(city)
        for com in coms:
            # 초기화: 모든 치킨집을 지운 후 com조합에 있는 치킨집을 살림
            for chicken in chicken_list:
                new_city[chicken[0]][chicken[1]] = 0
            for com_chicken in com:
                new_city[com_chicken[0]][com_chicken[1]] = 2

            # 해당 조합에 대해 치킨거리를 계산한 후 현재 최솟값보다 작으면 갱신
            temp = chicken_dist(new_city)
            if temp < dist:
                dist = temp
    
    return dist
    

def chicken_dist(arr):
    dist = 0
    homes = []
    chickens = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                homes.append((i, j))
            elif arr[i][j] == 2:
                chickens.append((i, j))
    
    # 각각의 집에 대해 치킨거리를 계산하여 합산
    for home in homes:
        temp = int(1e9)
        # 모든 치킨집 중에 가장 가까운 치킨집의 거리를 temp에 저장
        for chicken in chickens:
            distance = abs(chicken[0]-home[0]) + abs(chicken[1]-home[1])
            if distance < temp:
                temp = distance
        dist += temp
    
    return dist

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
print(chicken())