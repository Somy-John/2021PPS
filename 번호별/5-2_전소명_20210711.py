for i in range(int(input())):
    current = input().split()
    rst = float(current[0])
    for c in current[1:]:
        if c =="@": rst*=3
        elif c=="%": rst+=5
        elif c=="#": rst-=7
    print("%.2f"%rst)