import sys

sys.stdin = open("D2_1989_input.txt", "r")

t = int(input())

def check(word):
    result = 1    
    while word:
        if word[0] != word[-1]:
            return 0
        word = word[1:-1]
    return 1

for i in range(t):    
    letters = input()  
    print('#'+str(i+1), check(letters))