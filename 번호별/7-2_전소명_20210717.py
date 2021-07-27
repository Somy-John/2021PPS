eng = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
num = list(map(int,input().split()))
rst = []
for currentNum in range(num[0],num[1]+1):
    tmp = []
    for e in str(currentNum): tmp.append(eng[int(e)])
    rst.append(tmp)
rst.sort()
for currentNum in rst:
    tmp = ''
    for e in currentNum: tmp += str(eng.index(e))
    rst[rst.index(currentNum)] = tmp
for r in rst: print(r)