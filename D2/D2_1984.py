import sys

sys.stdin = open("D2_1984_input.txt", "r")

t = int(input())

for i in range(t):
    numbers = list(map(int, input().split()))
    numbers.sort()
    numbers = numbers[1:-1]
    result = round(sum(numbers)/len(numbers))

    print('#'+str(i+1), result)