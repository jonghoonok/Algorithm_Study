import sys

n = int(input())
ropes = [0]*n

for i in range(n):
    ropes[i] = int(sys.stdin.readline())

# 가장 견딜 수 있는 하중이 큰 로프부터 계산
ropes.sort(reverse=True)

result = 0
for i in range(n):
    if result < (i+1)*ropes[i]:
        result = (i+1)*ropes[i]

print(result)