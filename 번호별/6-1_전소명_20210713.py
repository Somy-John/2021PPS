from collections import deque
cards = deque(range(1,int(input())+1))
i = 0
while len(cards)>1:
    i+=1
    if i%2 == 1: cards.popleft()
    else: cards.rotate(-1)
print(cards[0])