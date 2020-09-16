N, M = map(int, input().split())
cur_list = [int(input()) for _ in range(N)]

d = [-1]*(M+1)
for cur in cur_list:
    if cur < M:
        d[cur] = 1

for i in range(1, M+1):
    if d[i] == -1:
        temp = 1000000
        for cur in cur_list:
            if i > cur and d[i-cur] != -1 and d[i-cur] + 1 < temp:        
                temp = d[i-cur] + 1
        if temp != 1000000:
            d[i] = temp

print(d[M])