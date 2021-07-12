num = input()
#1
print(int(bin(int(i:=num)*2)[3:],2) or i)
#2
n,m = int(num),1
while m<n:m*=2
print(n*2-m)