# 에라토스테네스의 체
def solution(n):
    arr = [False, False] + [True]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if arr[i]==True: 
            for j in range(i+i, n+1, i):
                arr[j] = False
    return arr.count(True)