n,k=map(int,input().split())
c,*a=range(n+1)
print(f'<{str([a.pop(c:=(c+k-1)%b)for b in a[::-1]])[1:-1]}>')