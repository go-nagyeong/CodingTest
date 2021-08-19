# 내가 푼 것
def solution(board, moves):
    basket = []
    j = -1
    result = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                j += 1
                break
        if len(basket) > 1:
            if basket[j-1] == basket[j]:
                del basket[j]
                del basket[j-1]
                j -= 2
                result += 2
    return result
  
# 더 좋은 방법
def solution(board, moves):
    pick = []
    answer = 0
    for x in moves:
        for i in range(len(board)):
            if board[i][x - 1] != 0:
                pick.append(board[i][x - 1])
                if len(pick) >= 2:
                    if pick[len(pick) - 1] == pick[len(pick) - 2]:
                        pick.pop()
                        pick.pop()
                        answer += 2
                board[i][x - 1] = 0
                break
    return answer
