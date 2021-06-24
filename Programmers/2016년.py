def solution(a, b):
    l = [31, 29, 31, 30, 31, 30,
         31, 31, 30, 31, 30, 31]
    day = sum(l[:a-1])-1+b
    dayweek = day%7
    w = ["FRI","SAT","SUN","MON",
         "TUE","WED","THU"]
    return w[dayweek]