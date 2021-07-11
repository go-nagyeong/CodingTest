def solution(s):
    dict_ = {'zero':'0', 'one':'1', 'two':'2', 
             'three':'3', 'four':'4', 'five':'5',
             'six':'6', 'seven':'7', 'eight':'8',
             'nine':'9'}
    for i in dict_.keys():
        if s.find(i) >= 0:
            s = s.replace(s[s.find(i):(s.find(i)+len(i))], dict_[i])
    return int(s)