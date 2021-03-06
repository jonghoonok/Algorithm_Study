cmd = input()
num_list = []
operation = []

# 먼저 input에서 숫자와 연산자를 분리하여 각각 num_list와 operation에 넣어줌
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

result = num_list[0]
flag = 0    
i = 0
temp = 0
# 그리디: operation을 따라 가면서 - 연산자가 나오면 이후에 등장하는 +로 이어지는 숫자들을 모두 더해 result에서 빼줌
# +연산자로 이어지고 있는 상황에서는 flag를 1로 해주고 아니면 0으로 해 줌
while i <len(operation):
    if flag == 0 and operation[i] == '+':
        result += num_list[i+1]
    elif flag == 0 and operation[i] == '-':
        flag = 1 - flag
        temp += num_list[i+1]
    elif flag !=0 and operation[i] == '+':
        temp += num_list[i+1]
    else:
        result -= temp
        temp = num_list[i+1]
    i += 1

result -= temp
print(result)