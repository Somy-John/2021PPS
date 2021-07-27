N = int(input())
rst = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            rst-=1
            break
print(rst)