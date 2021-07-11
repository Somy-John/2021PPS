row, column = map(int,input().split())
status = []
for i in range(5*row+1): status.append(input())
for b in status:
    if b == status[0]:
        