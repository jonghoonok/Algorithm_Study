def bin_search(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: return True, middle
        elif a[middle] < key: start = middle + 1
        else: end = middle - 1
    return False
# 재귀로 구현할 수도 있음

arr = [2, 3, 4, 7, 9, 11, 19, 23]
key = 17
print(bin_search(arr, key))