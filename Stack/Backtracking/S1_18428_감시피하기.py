from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(v):        
    # 상하좌우 각 방향으로 쭉 진행
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        while 0 <= nx < n and 0 <= ny < n:
            # 학생을 만나면 False를 리턴
            if school[nx][ny] == 'S':
                return False
            # X를 만나면 정상적으로 진행하는 것
            # 나가던 방향대로 좌표를 갱신하고 continue
            if school[nx][ny] == 'X':
                nx += dx[i]
                ny += dy[i]
                continue
            # 벽이나 선생님을 만나면 해당 방향으로 더이상 진행하지 않음
            if school[nx][ny] == 'O' or school[nx][ny] == 'T':
                break
    # 상하좌우 모든 방향으로 다 갔는데 학생을 안 만났으면 True
    return True


n = int(input())
school = [list(input().split()) for _ in range(n)]

teacher_list = []
hall_list = []
for i in range(n):
    for j in range(n):
        if school[i][j] == 'X':
            hall_list.append((i, j))
        elif school[i][j] == 'T':
            teacher_list.append((i, j))

# 모든 복도 중 3개를 고르는 조합
coms = list(combinations(hall_list, 3))
# 인쇄할 결과
result = 'NO'
for com in coms:
    # 벽 3개를 세움
    school[com[0][0]][com[0][1]] = 'O'
    school[com[1][0]][com[1][1]] = 'O'
    school[com[2][0]][com[2][1]] = 'O'

    flag = True
    # 모든 선생님들이 감시를 진행하게끔 반복
    for teacher in teacher_list:
        # 감시했는데 학생이 발견되면(False)
        # flag를 False로 바꿔주고 반복문 탈출
        if not dfs(teacher):
            flag = False
            break
    # 모든 선생님들이 학생을 발견하지 못하면 flag는 그대로(True)
    if flag == True:
        # 결과는 YES
        result = 'YES'
        # 더 이상의 조합을 볼 필요 없으니 break
        break
    
    # 다음 조합으로 넘어가기 위해 벽 3개를 치움
    school[com[0][0]][com[0][1]] = 'X'
    school[com[1][0]][com[1][1]] = 'X'
    school[com[2][0]][com[2][1]] = 'X'

print(result)