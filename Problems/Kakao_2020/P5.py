def time_sec(time):
    h, m, s = map(int, time.split(':'))
    result = h*3600 + m*60 + s
    return result


def sec_time(sec):
    HH = sec//3600
    MM = (sec-HH*3600)//60
    SS = sec-HH*3600 - MM*60
    if HH < 10:
        HH = '0'+str(HH)
    else:
        HH = str(HH)
    if MM < 10:
        MM = '0'+str(MM)
    else:
        MM = str(MM)
    if SS < 10:
        SS = '0'+str(SS)
    else:
        SS = str(SS)
    
    return HH+':'+MM+':'+SS


def solution(play_time, adv_time, logs):
    play_end = time_sec(play_time)
    
    log_list = [0]*(play_end+1)
    on_list = [0]*(play_end+1)
    off_list = [0]*(play_end+1)    
    for log in logs:
        start = time_sec(log[:8])
        end = time_sec(log[9:])        
        on_list[start] += 1
        off_list[end] += 1
    
    log_list[0] = on_list[0] - off_list[0]
    for i in range(1, play_end+1):
        log_list[i] = log_list[i-1] + on_list[i] - off_list[i]

    ad_end = time_sec(adv_time)
        
    accumulate = [0]*(play_end - ad_end + 1)
    accumulate[0] = sum(log_list[:ad_end])        
    
    for i in range(1, play_end - ad_end + 1):
        accumulate[i] = accumulate[i-1] + log_list[i-1+ad_end] - log_list[i-1]
    
    temp = 0
    ans = 0
    for i in range(len(accumulate)):
        if temp < accumulate[i]:
            temp = accumulate[i]
            ans = i
        
    answer = sec_time(ans)
    return answer


play1 = "02:03:55"
adv1 = "00:14:15"
log1 = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play1, adv1, log1))
play2 = "99:59:59"
adv2 = "25:00:00"
log2 = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play2, adv2, log2))
play3 = "50:00:00"
adv3 = "50:00:00"
log3 = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play3, adv3, log3))
