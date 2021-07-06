def solution(s, n):
    st = 'abcdefghijklmnopqrstuvwxyz'*2
    ST = st.upper()
    answer = ''
    for i in s:
        if i in ST:
            answer += ST[ST.index(i)+n]
        elif i in st:
            answer += st[st.index(i)+n]
        else:
            answer += ' '
    return answer

# 다른 방법
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n)
                       %26+ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n)
                       %26+ord('a'))
    return "".join(s)