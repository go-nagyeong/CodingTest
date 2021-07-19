def solution(participant, completion):
    participant.sort(); completion.sort()
    completion.append('')
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
          
# 더 좋은 방법 (해시 알고리즘)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer
