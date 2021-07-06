g = [4, 2]
s = [1, 2, 3]


def findContentChildren(g, s):
    g = sorted(g)
    s = sorted(s)
    output = 0
    i=0
    for grd in g:
        if i==len(s): break
        if grd <= s[i]:
            output+=1
            i+=1
        else:
            while True:
                if i==len(s)-1: break
                i+=1
                if grd <= s[i]:
                    output+=1
                    i+=1
                    break
    return output

print(findContentChildren(g,s))
