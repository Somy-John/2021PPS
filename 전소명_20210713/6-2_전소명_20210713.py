n,k=map(int,input().split())
*p,i=list(range(1,n+1))+[0]
print("<",end='')
while len(p)>1:print(p.pop(i := i+k-1 if (i+k-1)<len(p) else (i+k-1)%len(p)),end=", ")
print(f'{p[0]}>')