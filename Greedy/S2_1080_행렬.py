def operation():
    # 먼저 n,m중 하나라도 3보다 작으면 연산이 불가하므로 같은지만 체크
    if n < 3 or m < 3:
        for i in range(n):
            for j in range(m):
                if a[i][j] != b[i][j]:
                    return -1
        return 0        
    
    ans = 0
    # a행렬의 좌상단부터 돌면서 하나씩 b와 다르면 바꿔줌
    # 좌상단(0, 0)은 단 하나의 부분행렬에만 포함됨: 한 번 바꾸면 다시는 바꿀 일이 없음
    # (0, 0)이 완료되면, (0, 1)이 "변환이 완료되지 않은 행렬"의 좌상단이 됨
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                ans += 1
                for k in range(3):
                    for l in range(3):
                        a[i+k][j+l] = 1- a[i+k][j+l]

    # 변환이 완료되면 한 바퀴 돌면서 검사하고, 같지 않은 부분이 있으면 변환 불가한 것으로 -1을 리턴한 후 종료
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return -1

    return ans


n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    row = list(map(int, input()))
    a.append(row)
for _ in range(n):
    row = list(map(int, input()))
    b.append(row)

print(operation())