cmd = input()
num_list = []
operation = []

i = 0
j = 0
while j <= len(cmd):
    if j == len(cmd):
        num_list.append(int(cmd[i:j]))
        break
    if cmd[j] in ['+', '-']:
        num_list.append(int(cmd[i:j]))
        operation.append(cmd[j])
        i = j + 1
    j += 1
print(num_list)
print(operation)

result = num_list[0]
cnt = 0    
i = 0
temp = 0
while i <len(operation):
    if cnt == 0 and operation[i] == '+':
        result += num_list[i+1]
    elif cnt == 0 and operation[i] == '-':
        cnt += 1
        temp += num_list[i+1]
    elif cnt !=0 and operation[i] == '+':
        temp += num_list[i+1]
    else:
        result -= temp
        temp = 0
    i += 1
result -= temp
print(result)