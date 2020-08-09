#가위1 바위2 보3

a, b = map(int, input().split())
if (a, b) == (1, 2):
    print('B')
elif (a, b) == (1, 3):
    print('A')
elif (a, b) == (2, 1):
    print('A')
elif (a, b) == (2, 3):
    print('B')
elif (a, b) == (3, 1):
    print('B')
elif (a, b) == (3, 2):
    print('A')