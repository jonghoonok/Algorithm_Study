import sys

n = int(input())
wines = [0]*n
for i in range(n):
    wines[i] = int(sys.stdin.readline())

# 연속으로 몇 잔을 마셨는지에 따라 해당 인덱스까지 최대로 마실 수 있는 와인의 양을 표기함
# 인덱스 0: 이번엔 안 마심, 1: 직전 인덱스에 안 마심, 2: 그 다음 잔을 마실 수 없음
drink = [[0, 0, 0] for _ in range(n)]
drink[0][1] = wines[0]
if n > 1:
    drink[1][0] = drink[0][1]
    drink[1][1] = wines[1]
    drink[1][2] = drink[0][1] + wines[1]
    for i in range(2, n):
        # 이번엔 안 마심
        drink[i][0] = max(drink[i-1])
        # 직전 인덱스의 와인을 안 마심
        drink[i][1] = max(drink[i-2]) + wines[i]
        # 직전 인덱스의 와인을 마심
        drink[i][2] = drink[i-1][1] + wines[i]
    
print(max(drink[n-1]))
    