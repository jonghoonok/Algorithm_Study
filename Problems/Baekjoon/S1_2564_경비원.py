def min_dist():
    result = 0
    
    # 해당 구역을 한바퀴 돌면 나오는 거리
    loop = 2*(width + height)
    # 원점으로부터 나까지의 거리
    my_location = calc_dist(my_dir, my_dist)
    
    for i in range(n):
        # 원점으로부터 target까지의 거리
        target_location = calc_dist(shops[i][0], shops[i][1])

        # 나까지의 거리와 target까지 거리의 차를 구한다
        temp = target_location - my_location if target_location > my_location else my_location - target_location

        # 거리의 차는 loop의 절반보다 클 수도 있고 작을 수도 있음
        # 작으면 시계방향으로 target까지 가는 것이 반시계보다 빠르다는 얘기: 그대로 더함
        # 크면 반시계방향이 더 빠르다는 얘기이므로 loop에서 이 값을 빼서 더함
        temp2 = temp if temp < loop / 2 else loop - temp
        
        result += temp2

    return result

# 원점으로부터 대상까지의 거리를 시계방향으로 계산
def calc_dist(x, y):
    if x == 1:
        return y
    elif x == 4:
        return width + y
    elif x == 2:
        return width + height + (width - y)
    else:
        return 2*(width + height) - y


width, height = map(int, input().split())
n = int(input())
shops = [[0, 0] for _ in range(n)]
for i in range(n):
    dir, dist = map(int, input().split())
    shops[i][0], shops[i][1] = dir, dist
my_dir, my_dist = map(int, input().split())

print(min_dist())