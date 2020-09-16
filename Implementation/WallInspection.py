from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    answer = len(dist)+1
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1       # 투입할 친구의 수
            # 투입한 친구가 1시간동안 갈 수 있는 곳
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어난 경우
                if position < weak[index]:
                    count += 1      # 친구 추가 투입
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer