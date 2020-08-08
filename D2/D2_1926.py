n = int(input())

def count369(a):
    a = str(a)
    cnt = 0
    for j in range(len(a)):
        if a[j] in ('3', '6', '9'):
            cnt += 1
    return cnt

for i in range(1, n+1):    
    cnt = count369(i)
    if cnt == 0:
        print(i, end = ' ')
    else:
        print('-'*cnt, end = ' ')