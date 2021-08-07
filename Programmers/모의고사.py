# 내가 푼 것 (코드는 길지만, 수행속도는 더 빠름)
def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    i = j = k = 0
    score = [0, 0, 0]
    for answer in answers:
        try:
            if answer == one[i]:
                score[0] += 1
        except:
            i = 0
            if answer == one[i]:
                score[0] += 1
        try:
            if answer == two[j]:
                score[1] += 1
        except:
            j = 0
            if answer == two[j]:
                score[1] += 1
        try:
            if answer == three[k]:
                score[2] += 1
        except:
            k = 0
            if answer == three[k]:
                score[2] += 1
        i += 1; j += 1; k += 1

    result = []
    if score.count(max(score)) == 1:
        result.append(score.index(max(score))+1)
    else:
        for i in range(len(score)):
            if score[i] == max(score):
                result.append(i+1)

    return result


# 다른 방법 (코드는 짧지만, 수행 속도는 더 느림)
def solution(answers):
    counts = [0,0,0]
    winner = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    
    for i in range(len(answers)):
        if answers[i] == s1[(i%5)]:
            counts[0] += 1
        if answers[i] == s2[(i%8)]:
            counts[1] += 1
        if answers[i] == s3[(i%10)]:
            counts[2] += 1
            
    for i in range(3):
        if counts[i] == max(counts):
            winner.append(i+1)

    return winner
