string = input()
word = input()
n = len(string)
m = len(word)
lastChar = word[-1]

stack = []

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-m:]) == word:
        del stack[-m:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")