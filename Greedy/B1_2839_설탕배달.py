def sugar(num):
    div_5 = num // 5
    remain_5 = num % 5
    if not remain_5:
        return div_5
    else:
        if remain_5 == 3:
            return 1 + div_5
        else:
            if div_5 >= 1:
                if remain_5 == 1:
                    return 2 + (div_5 - 1)
                elif remain_5 == 2:
                    if div_5 >= 2:
                        return 4 + (div_5 - 2)
                    else:
                        return -1
                else:
                    return 3 + (div_5 - 1)
            else:
                return -1


n = int(input())
print(sugar(n))