# 풀이1: 모든 키를 더한 값과 100의 차를 합으로 갖는 페어를 브루트포스로 찾기
# O(n^2)

def dwarf1():
    flag = 0
    fake_1, fake_2 = 0, 0
    for i in range(9):
        for j in range(i+1, 9):
            if heights[i] + heights[j] == target:
                fake_1, fake_2 = i, j
                break
        if flag == 1:
            break

    true_heights = [0 for _ in range(9)]
    for i in range(9):
        if i != fake_1 and i != fake_2:
            true_heights[i] = heights[i]

    true_heights.sort()
    for i in range(2, 9):
        print(true_heights[i])

# 풀이2: 1과 비슷하나 미리 정렬을 하고 O(nlogn), 정렬된 키에서 양쪽으로 하나씩 줄이며 페어를 찾음 O(n)
def dwarf2():
    heights.sort()

    i, j = 0, 8
    while(i != j):
        temp = heights[i] + heights[j]
        if temp > target:
            j -= 1
            continue
        elif temp < target:
            i += 1
            continue
        else:
            break

    for k in range(i):
        print(heights[k])
    for k in range(i+1, j):
        print(heights[k])
    for k in range(j+1, 9):
        print(heights[k])


heights = [0 for _ in range(9)]

for i in range(9):
    heights[i] = int(input())

target = sum(heights) - 100

# dwarf1()
dwarf2()