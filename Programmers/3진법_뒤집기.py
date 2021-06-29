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

# 더 좋은 방법
def solution(n):
    rev = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev += str(mod)
    return int(rev, 3)