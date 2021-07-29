s = input()
rst = []
for i in range(len(s)): 
    for j in range(len(s)-i):
        rst.append(s[i:i+j+1])
print(len(set(rst)))