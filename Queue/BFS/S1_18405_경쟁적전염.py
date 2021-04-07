from collections import deque


def infection(s, x, y):
    # 바이러스의 번호와 x, y좌표를 리스트에 저장
    viruses = []
    for i in range(n):
        for j in range(n):
            if test_tube[i][j]:
                viruses.append([test_tube[i][j], i, j])
    
    # 번호 순서대로 저장하기 위해 정렬 후 덱에 삽입
    viruses.sort()
    virus_list = deque()
    for virus in viruses:
        virus_list.append(virus)    

    # 1초에 한 번씩 바이러스를 증식시켜 s초가 될 때까지 반복
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for time in range(s):
        # virus의 번호가 낮은 순서대로 시작
        i = 0
        length = len(virus_list)
        while i < length: 
            virus = virus_list[i]       
            # 상하좌우 방향으로 시험관이 비어있으면 증식
            for j in range(4):
                nx = virus[1] + dx[j]
                ny = virus[2] + dy[j]
                if 0 <= nx < n and 0 <= ny < n and test_tube[nx][ny] == 0:
                    test_tube[nx][ny] = virus[0]
                    # 1초가 지난 후에 증식된 위치로부터 시작할 수 있게 virus_list에 추가
                    virus_list.append([virus[0], nx, ny])
            i += 1
        # 한 사이클이 다 돌았으면 기존 virus_list 요소들을 버림
        for _ in range(length):
            virus_list.popleft()
    
    return test_tube[x-1][y-1]


n, k = map(int, input().split())
test_tube = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
print(infection(s, x, y))