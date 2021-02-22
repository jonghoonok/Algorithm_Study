def color(x, y):
    for i in range(10):
        for j in range(10):
            white[x+i][y+j] = 1


def colored():
    result = 0
    for i in range(100):
        for j in range(100):
            if white[i][j]:
                result += 1
    return result


white = [[0]*100 for _ in range(100)]   # 100*100 사이즈의 흰색 도화지

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    color(x, y)     # 흰색 도화지에 색을 칠함

print(colored())