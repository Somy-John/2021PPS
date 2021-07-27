rst = ''
for c in input(): rst+=chr(ord(c)+((-3)if ord(c)>ord('C') else (+23)))
print(rst)