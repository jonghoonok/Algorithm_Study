import sys

sys.stdin = open("D3_1234_input.txt", "r")


def password_change(numbers):
    password = str(numbers)
    while password:
        i = 0
        m = len(password)
        for i in range(len(password)-1):
            if password[i] == password[i+1]:                
                password = password[:i]+password[i+2:]
                break
        if len(password) == m:
            return password

for test_case in range(10):
    n, numbers = input().split()
    n = int(n)
    print('#' + str(test_case + 1), password_change(numbers))
