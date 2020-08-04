import sys

sys.stdin = open("D3_1208_input.txt", "r")


# 리스트 내에 가장 큰 값이 있는 인덱스 반환
def my_max_index(inputlist):
    temp = 0
    my_index = 0
    for i in range(100):
        if inputlist[i] >= temp:
            temp = inputlist[i]
            my_index = i
    return my_index


def my_min_index(inputlist):
    temp = 100      # 상자의 높이는 최대 100이므로 초깃값 100으로 설정
    my_index = 0
    for i in range(100):
        if inputlist[i] <= temp:
            temp = inputlist[i]
            my_index = i
    return my_index


for test_case in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))
    # 완전탐색: 가장 상자가 많은 부분에서 가장 적은 부분으로 하나씩 옮기는 것을 dump 만큼 반복
    while dump:
        box_list[my_max_index(box_list)] -= 1
        box_list[my_min_index(box_list)] += 1
        dump -= 1
    result = box_list[my_max_index(box_list)] - box_list[my_min_index(box_list)]

    print('#'+str(test_case), result)
