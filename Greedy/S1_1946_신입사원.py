import sys

t = int(input())
for _ in range(t):
    n = int(input())
    candidates = [[0, 0] for _ in range(n)]
    for i in range(n):
        resume, interview = map(int, sys.stdin.readline().split())
        candidates[i][0], candidates[i][1] = resume, interview
 
    candidates.sort()
    
    # 서류 1등의 면접 순위를 기준점으로 삼음
    border = candidates[0][1]
    result = 1

    # 서류 2~n등에 대해 면접 순위가 border보다 높은 사람을 합격시킴
    for i in range(1, n):
        if candidates[i][1] < border:
            border = candidates[i][1]
            result += 1

    print(result)