class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b): b = '0'*(len(a)-len(b))+b
        elif len(b)>len(a): a = '0'*(len(b)-len(a))+a
        a = "".join(reversed(list(a)))
        b = "".join(reversed(list(b)))
        rst = ''
        tmp = 0
        for i in range(len(a)):
            n,m = a[i],b[i]
            c = int(n)+int(m)+tmp
            tmp=0
            if c==0: rst+='0'
            elif c==1: rst+='1'
            elif c==2: 
                rst+='0'
                tmp=1
            elif c==3:
                tmp=1
                rst+='1'
        if c==3 or c==2: rst+='1'
        return "".join(reversed(list(rst)))