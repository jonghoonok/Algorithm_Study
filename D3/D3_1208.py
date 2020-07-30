import sys

sys.stdin = open("D3_1208_input.txt", "r")

for test_case in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))
    while dump:        
        box_list[box_list.index(max(box_list))] -= 1
        box_list[box_list.index(min(box_list))] += 1
        dump -=1           
    result = max(box_list) - min(box_list)
    print('#'+str(test_case), result)