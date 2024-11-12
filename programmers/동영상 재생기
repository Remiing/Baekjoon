# https://school.programmers.co.kr/learn/courses/30/lessons/340213

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = str2num(video_len)
    pos = str2num(pos)
    op_start = str2num(op_start)
    op_end = str2num(op_end)
    
    for command in commands:
        pos = op_end if op_start <= pos <= op_end else pos
        if command == 'prev':
            if pos < 10:
                pos = 0
            else:
                pos -= 10
        else:
            if video_len - pos < 10:
                pos = video_len
            else:
                pos += 10
                
    pos = op_end if op_start <= pos <= op_end else pos
    return f'{str(pos//60).zfill(2)}:{str(pos%60).zfill(2)}'
    
    
def str2num(str_time):
    int_time = int(str_time[0:2])*60 + int(str_time[3:5])
    return int_time


# else
#        if command == "prev":
#            current_pos = max(0, current_pos - 10)
#        elif command == "next":
#            current_pos = min(video_len, current_pos + 10)
