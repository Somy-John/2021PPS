n,k=map(int,input().split())
p=list(range(1,n+1))
i = 0
r=[]
while len(p)>0:
    i = i+k-1 if (i+k-1)<len(p) else (i+k-1)%len(p)
    r.append(p.pop(i))
print("<",end='')
for j in r[:-1]: print(j,end=", ")
print(f'{r[-1]}>')