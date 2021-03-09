n = int(input())

n = 1000 - n
result = 0

coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    result += n // coin
    n = n % coin

print(result)