n = int(input())
coins = sorted(list(map(int, input().split())))

money = set()
for coin in coins:
    money.add(coin)
    for i in money:
        money.add(i+coin)

target = 1
while True:
    if target in money:
        target += 1
    else:
        print(target)
        break

# 더 간결한 풀이
target = 1
for x in coins:
    if target < x:
        break
    else:
        target += x
print(target)