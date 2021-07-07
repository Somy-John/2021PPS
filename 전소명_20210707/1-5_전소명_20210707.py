def plusOne(digits):
    return list(map(int,str(int("".join(map(str,digits)))+1)))

print(plusOne([1,2,3]))