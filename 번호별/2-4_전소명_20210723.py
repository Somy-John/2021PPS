dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
rst = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            rst += dial.index(i)+3
print(rst)
