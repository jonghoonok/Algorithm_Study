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

result = 0
cnt = 0
for i in range(len(operation)):
    temp = 0
    if cnt == 0 and operation[i] == '-':
        result += sum(num_list[:i+1])
        cnt = i+1
        continue
    if cnt != 0 and operation[i] == '-':
        result -= sum(num_list[cnt:i+1])
        cnt = i+1
    