passWords = list()
rstList = list()
while (tmp := input())!= 'end': passWords.append(tmp)
for passWord in passWords:
    rst = True
    for i in ['a','e','i','o','u']:
        if passWord.count(i)<1: rst = False
        else: 
            rst = True
            break
    ac,bc = 0,0
    for i in passWord:
        if i in ['a','e','i','o','u']: 
            ac+=1
            bc=0
        else: 
            ac = 0
            bc += 1
        if ac==3 or bc==3:
            rst = False
            break
    for i in set(passWord):
        if passWord.count(i*2)>0 and i not in ['e','o']: rst = False
    rstList.append(f'<{passWord}> is {""if rst else "not "}acceptable.')
for r in rstList: print(r)