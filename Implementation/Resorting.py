def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


chars = list(input())

alphas = []
nums = []
for char in chars:
    word_to_num = ord(char)
    if 65 <= word_to_num < 91:
        alphas.append(word_to_num)
    else:
        nums.append(int(char))

new_alphas = quick_sort(alphas)
num = sum(nums)

for i in range(len(new_alphas)):
    new_alphas[i] = chr(new_alphas[i])

result = ''.join(new_alphas) + str(num)
print(result)