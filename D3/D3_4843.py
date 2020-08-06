import sys

sys.stdin = open("D3_4843_input.txt", "r")


def special_sort(n, numbers):
    # selection sort
    for i in range(1, n):
        key = numbers[i]
        j = i-1
        while numbers[j] > key and j >= 0:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key

    # 홀수번과 짝수번 원소를 번갈아가며 새로운 리스트에 추가
    new_numbers = []
    for i in range(1, n+1):
        if i % 2 == 0:
            new_numbers.append(numbers[i//2 - 1])
        else:
            j = (i + 1)//2
            new_numbers.append(numbers[-j])

    return ' '.join(map(str, new_numbers[:10]))

t = int(input())

for test in range(t):
    n = int(input())
    numList = list(map(int, input().split()))
    print('#' + str(test + 1), special_sort(n, numList))
