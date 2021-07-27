testCase = []
for i in range(int(input())): testCase.append(input())
rst = []
for i in range(len(testCase)):
    score, tmp = 0,0
    for j in testCase[i]:
        if j == "O":
            tmp+=1
            score += tmp
        else: 
            tmp = 0
    rst.append(score)
for i in rst: print(i)