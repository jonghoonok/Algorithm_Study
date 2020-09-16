s = list(map(int, input()))

cnt = 0
temp = s[0]

for i in range(1, len(s)):
    if s[i] != temp:
        temp = s[i]
        cnt += 1

result = (cnt-1)//2 + 1
print(result)