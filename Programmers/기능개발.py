def solution(progresses, speeds):
    answer = []
    w\hile len(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        j = 0
        while j < len(progresses):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
                j -= 1
            else:
                break
            j += 1
        if count > 0:
            answer.append(count)
    return answer
