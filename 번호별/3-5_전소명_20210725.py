N, firstDay = map(int,input().split())
gg, gb, bg, bb = map(float,input().split())
gCount = [0 for _ in range(N)]
bCount = [0 for _ in range(N)]
if firstDay == 0:
    gCount[0] = gg
    bCount[0] = gb
else:
    gCount[0] = bg
    bCount[0] = bb

for _ in range(1,N):
    gCount[_] = gCount[_-1]*gg + bCount[_-1]*bg
    bCount[_] = gCount[_-1]*gb + bCount[_-1]*bb

print(round(gCount[N-1]*1000))
print(round(bCount[N-1]*1000))