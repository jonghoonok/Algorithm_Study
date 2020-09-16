n, m = map(int, input().split())
balls = list(map(int, input().split()))

array = [0]*11

for ball in balls:
    array[ball] += 1

result = 0
for i in range(1, m+1):
    for j in range(i+1, m+1):
        result += array[i]*array[j]
    
# 이렇게 계산하면 더 빠름
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i]*n