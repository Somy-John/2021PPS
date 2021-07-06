testCase = []
for i in range(int(input())): testCase.append(list(map(int,input().split())))
rst = []
for case in testCase:
    count = 0
    caseRst = list(map(lambda x: x>int(int(sum(case[1:])/case[0])), case))[1:]
    for std in caseRst: 
        if std: count+=1
    rst.append(count/float(len(caseRst))*100)
for resert in rst: print("%.3f" % resert+'%')