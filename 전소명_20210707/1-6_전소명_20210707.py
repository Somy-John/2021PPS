def generate(numRows):
    rst = []
    for i in range(numRows):
        if i == 0: rst.append([1])
        elif i==1 : rst.append([1,1])
        else:
            tmp = [1]
            for j in range(len(rst[-1])-1): tmp.append(rst[-1][j]+rst[-1][j+1])
            tmp.append(1)
            rst.append(tmp)
    return rst

print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(5))