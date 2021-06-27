def solution(n):
    ternary = []
    while n >= 3:
        ternary.append(n%3)
        n = n//3
    ternary.append(n)
    ternary.reverse()
    
    answer = 0
    for i in range(len(ternary)):
        answer += ternary[i] * pow(3, i)
    return answer