# Pythonic
num = list(map(int, input()))
m = len(num)//2

temp1 = 0
temp2 = 0
for i in range(m):
    temp1 += num[i]
    temp2 += num[m+i]

if temp1 == temp2:
    print('LUCKY')
else:
    print('READY')
