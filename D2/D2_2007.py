import sys

sys.stdin = open("D2_2007_input.txt", "r")

t = int(input())

def check(words):
    cnt = 1
    while True:
        word = words[:cnt]
        temp = words[cnt:cnt*2]
        if word == temp: return cnt
        else: cnt += 1

for test_case in range(t):
    words = input()   
    print('#'+str(test_case+1), check(words))