def solution(cookie):
    answer = []
    bnum = len(cookie)
    for i in range(0,bnum):
        sum1,sum2=[],[]
        for j in range(i+1): sum1.append(sum(cookie[j:i+1]))
        for j in range(i+1,bnum): sum2.append(sum(cookie[i+1:j+1]))
        for rst in sum1:
            if rst in sum2: answer.append(rst)
    return max(answer) if len(answer)!=0 else 0