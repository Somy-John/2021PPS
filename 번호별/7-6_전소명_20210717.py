rst = []
for i in range(int(input())): rst.append(list(map(int,input().split())))
for r in sorted(rst): print(r[0],r[1])