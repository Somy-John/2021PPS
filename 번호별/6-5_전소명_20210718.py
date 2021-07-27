input()
rst = sorted(list(set(list(map(int,input().split())))))
for i in rst[:-1]: print(i,end = ' ')
print(rst[-1])