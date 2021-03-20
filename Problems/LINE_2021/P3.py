from collections import deque
from itertools import combinations

    n = len(enter)

    contact = [[0]*(n+1) for _ in range(n+1)]
    room = deque()
    # room.append(enter[0])

    j = 0
    for i in range(n):
        room.append(enter[i])

        while(leave[j] in room):
            room.remove(leave[j])
            j += 1

        # 더 이상 나갈 사람이 없으면 만나는 리스트 갱신하고 다음 사람을 받음
        for com in list(combinations(room, 2)):
            contact[com[0]][com[1]] = 1
            contact[com[1]][com[0]] = 1

    result = [0]*n
    for i in range(1, n+1):
        for j in range(1, n+1):
            if contact[i][j]:
                result[i-1] += 1