rst = []
for i in range(10):
    m = int(input())%42
    if m not in rst: rst.append(m)
print(len(rst))