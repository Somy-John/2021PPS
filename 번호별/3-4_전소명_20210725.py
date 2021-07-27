N = int(input())
s = int(input())
if N <= 5:
    for _ in range(N-1):
        s = int(not s)
        print(s)
else:
    print("Love is open door")