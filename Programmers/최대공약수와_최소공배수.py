def solution(n, m):
    answer = []
    # 최대공약수
    a = []
    for i in range(1, max(n, m)+1):
        if n % i == 0 and m % i == 0:
            a.append(i)
    answer.append(max(a))
    # 최소공배수
    b = []
    for i in range(1, (n*m)+1):
        if i % n == 0 and i % m == 0:
            b.append(i)
    answer.append(min(b))
    return answer

# 더 좋은 방법
# (코드는 더 간단하지만 수행 시간은 더 오래걸림)
from math import gcd
def solution(n, m):
    return [gcd(n,m), (n*m)//gcd(n,m)]