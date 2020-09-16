def solution(food_times, K):
    time = 1
    while time <= K:
        i = time % len(food_times)
        if food_times[i-1]:
            food_times[i-1] -= 1                    
        time += 1
    result = time % len(food_times)
    return result