N = int(input())
food_list = list(map(int, input().split()))

d = [0]*(N)
d[0] = food_list[0]
d[1] = food_list[1]

for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+food_list[i])

print(d[N-1])
