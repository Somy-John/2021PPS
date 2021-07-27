n, li = int(input()),[]
for i in range(n): li.append(input())
for i in range(n):
    for j in range(n-i-1):
        if len(li[j]) > len(li[j+1]):
                li[j], li[j+1] = li[j+1], li[j]
        elif len(li[j]) == len(li[j+1]):
            tmp1,tmp2=0,0
            for e1 in li[j]:
                if e1.isdecimal(): tmp1+=int(e1)
            for e2 in li[j+1]:
                if e2.isdecimal(): tmp2+=int(e2)
            if tmp1>tmp2:
                li[j], li[j+1] = li[j+1], li[j]
            elif tmp1==tmp2:
                if li[j] > li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]
for i in li:print(i)