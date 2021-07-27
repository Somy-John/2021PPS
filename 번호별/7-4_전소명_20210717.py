rst = []
string = input()
for i in range(0,len(string)): rst.append(string[i:])
for r in sorted(rst): print(r)