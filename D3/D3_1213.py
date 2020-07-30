import sys

sys.stdin = open("D3_1213_input.txt", "r", encoding='UTF8')

for test_case in range(1, 11):
    n = int(input())
    word = input()
    words = input()
    result = 0
    word_len = len(word)
    while words:
        if word == words[:word_len]:
            result += 1
            words = words[word_len:]
        else:
            words = words[1:]
        if len(words) < word_len: break
    print('#'+str(test_case), result)