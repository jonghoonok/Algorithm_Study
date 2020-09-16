n = int(input())
explorers = list(map(int, input().split()))

group = 0
temp = 0
for i in range(1, n+1):
    cnt = (explorers.count(i)+temp) // i
    group += cnt
    temp = cnt % i

print(group)

# count는 오래걸리기 때문에 sort해준 후 앞에서부터 계산하는 것이 빠름