# 문제를 잘못읽었는데 다시 풀기에는 귀찮아서 방치함..
def solution(n, build_frame):
    answer = []    
    
    for cmd in build_frame:
        # 설치
        if cmd[3]:
            x, y = cmd[0], cmd[1]
            # 기둥 설치
            if not cmd[2]:
                # 바닥 위에 있거나 밑에 다른 기둥이 있으면 설치
                if y == 0 or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                    answer.append([x, y, 0])                
            # 보 설치
            else:
                # 양쪽에 보가 있거나 둘 중 하나에 기둥이 있으면 설치
                if ([x-1, y, 1] in answer and [x+1, y, 1] in answer) or [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                    answer.append([x, y, 1])
        # 제거
        else:            
            re_move(answer, cmd[:3])
            # 제거한 후에 유효성 검사를 하여 조건이 안 맞으면 빼야 함

    answer.sort()
    
    return answer


# 기둥과 보를 제거했을 때 그에 따라 제거되는 부분을 재귀적으로 제거
def re_move(arr, cmd):
    x, y = cmd[0], cmd[1]
    arr.remove(cmd)
    # 기둥 제거: 위의 기둥과 보를 체크
    if not cmd[2]:
        # 위 기둥
        if [x, y+1, 0] in arr and [x, y+1, 1] not in arr and [x-1, y+1, 1] not in arr:
            re_move(arr, [x, y+1, 0])
        # 왼쪽 위 보
        if [x-1, y+1, 1] in arr and [x, y+1, 1] not in arr:
            re_move(arr, [x-1, y+1, 1])
        # 오른쪽 위 보
        if [x, y+1, 1] in arr and [x-1, y+1, 1] not in arr:
            re_move(arr, [x, y+1, 1])
    # 보 제거: 양 옆의 보와 보 위의 기둥을 체크
    else:
        # 오른쪽 위 기둥
        if [x+1, y, 0] in arr and [x+1, y, 1] not in arr and [x+1, y-1, 0] not in arr:
            re_move(arr, [x+1, y, 0])
        # 위 기둥
        if [x, y, 0] in arr and [x-1, y, 1] not in arr and [x, y-1, 0] not in arr:
            re_move(arr, [x, y, 0])
        # 왼쪽 보
        if [x-1, y, 1] in arr and [x-1, y-1, 0] not in arr and [x, y-1, 0] not in arr and [x-2, y, 1] not in arr:
            re_move(arr, [x-1, y, 1])
        # 오른쪽 보
        if [x+1, y, 1] in arr and [x+1, y-1, 0] not in arr and [x+2, y-1, 0] not in arr and [x+2, y, 1] not in arr:
            re_move(arr, [x+1, y, 1])


build = input().split(',')
n = int(build[0])


command = []
i = 1
while i < len(build):
    temp = []
    for j in range(4):
        if len(build[i+j]) >= 3:
            if build[i+j][1] == '[':
                if len(build[i+j]) == 4:
                    x = int(build[i+j][3])
                else:
                    x = int(build[i+j][2])
            else:                
                y = int(build[i+j][1])                
        else:
            temp.append(int(build[i+j][1]))
    command.append([x, temp[0], temp[1], y])

    i += 4

print(solution(n, command))