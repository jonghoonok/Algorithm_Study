t = int(input())
for num in range(t+1):
    if num == t:
        print(t-num)
        break     
    print(t-num, end = " ")
    