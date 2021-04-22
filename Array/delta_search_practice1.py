def delta_search(arr):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = 0

    for x in range(N):
        for y in range(N):
            for i in range(4):
                testX = x + dx[i]
                testY = y + dy[i]                
                if 0 <= testX < N and 0 <= testY < N:
                    difference = arr[x][y] - arr[testX][testY]
                    if difference >= 0: result += difference
                    else:               result -= difference
    return result

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(delta_search(arr))