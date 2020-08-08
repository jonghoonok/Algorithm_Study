import sys
import base64

sys.stdin = open("D2_1928_input.txt", "r")

t = int(input())

for i in range(t):
    baseSentence = input()
    temp = base64.b64decode(baseSentence.encode("UTF-8"))
    transformedSentence = temp.decode("UTF-8")
    print('#'+str(i+1), transformedSentence)