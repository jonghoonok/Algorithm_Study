import sys

n, m = map(int, sys.stdin.readline().split())
word_set = {}

for i in range(n):
    word = sys.stdin.readline()
    word_set[word] = i

result = 0
for _ in range(m):
    word = sys.stdin.readline()
    if word in word_set:
        result += 1

print(result)