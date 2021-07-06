def solution(strings, n):
    a = []
    for i in strings:
        a.append(i[n])
    answer = []
    for j in sorted(set(a)):
        for k in sorted(strings):
            if j == k[n]:
                answer.append(k)
    return answer

# 더 좋은 방법 1
def solution(strings, n):
    return sorted(sorted(strings), 
                  key=lambda x:x[n])

# 더 좋은 방법 2
def solution(string, n):
    li_ = []
    for i in range(len(string)):
        string[i] = string[i][n] + string[i]
    string.sort()
    for i in range(len(string)):
        li_.append(string[i][1:])
    return li_