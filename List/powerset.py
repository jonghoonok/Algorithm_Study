def printList(arr, bit):
    for i in range(len(bit)):
        if bit[i]:
            print(arr[i], end = ' ')
    print()

arr = [1, 2, 3]
bit = [0] * 3

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            printList(arr, bit)
