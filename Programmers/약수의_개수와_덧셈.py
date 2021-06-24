def solution(left, right):
    count = 0
    answer = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
        count = 0
    return answer

# 더 좋은 방법
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        # 제곱근 값이 정수이면 약수의 개수가 홀수
        if (i**0.5) == int(i**0.5):
            answer -= i
        else:
            answer += i
    return answer