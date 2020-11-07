import sys

sys.stdin = open("D5_1247_최적경로_input.txt", "r")

# 현재까지 움직인 거리 dist, 현재 좌표 x, y 방문한 고객의 수 k
def path(dist, x, y, k):
    global ans

    # n명의 고객을 다 방문한 후 집까지의 거리 계산
    if k == n:
        curdist = abs(x-location[2]) + abs(y-location[3])
        if dist + curdist < ans:
            ans = dist + curdist
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            # 현재 좌표에서 i번 고객의 집까지의 거리 curdist
            curdist = abs(x-location[(i+2)*2]) + abs(y-location[(i+2)*2+1])
            # 이동했을 때 거리가 ans보다 작을 경우에만 이동
            if dist + curdist < ans:
                path(dist + curdist, location[(i+2)*2], location[(i+2)*2+1], k+1)
            visit[i] = 0

    
t = int(input())    
for test_case in range(t):    
    n = int(input())
    location = list(map(int, input().split()))  
    visit = [0]*n    
    ans = int(1e9)  
    path(0, location[0], location[1], 0)
    print('#' + str(test_case + 1), ans)