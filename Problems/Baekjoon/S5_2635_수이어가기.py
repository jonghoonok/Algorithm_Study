def num_continue(a, b):
    temp = a - b
    if temp < 0:
        return 2
    else:
        return 1 + num_continue(b, temp)


def fill_ans(arr):
    temp = arr[-2] - arr[-1]
    if temp < 0:
        return arr
    else:
        return fill_ans(arr + [temp])


n = int(input())
result = 0
ans = []

for i in range(n, n//2, -1):
    temp = num_continue(n, i)
    if temp > result:
        result = temp
        ans = fill_ans([n, i])

print(result)
print(' '.join(map(str, ans)))