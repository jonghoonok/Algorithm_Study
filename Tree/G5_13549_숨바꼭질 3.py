from collections import deque

n, k = map(int, input().split())

time = [-1]*100001
time[n] = 0
q = deque([n])
while q:
    num = q.popleft()
    
    if num == k:
        print(time[num])
        break
    
    if num < 50001 and time[num*2] == -1:
        time[num*2] = time[num]
        q.appendleft(num*2)      # 순간이동 : 우선순위가 높기 때문에 큐의 앞에 배치
    if 0 < num+1 < 100001 and time[num+1] == -1:
        time[num+1] = time[num]+1
        q.append(num+1)         # 걷기
    if 0 <= num-1 < 100001 and time[num-1] == -1:
        time[num-1] = time[num]+1
        q.append(num-1)         # 걷기