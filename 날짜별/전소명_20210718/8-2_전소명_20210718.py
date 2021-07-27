# from itertools import combinations
# n,k = 4,2
# scores = []
# for i in [20, 50, 30, 30]: scores.append(int(i))
# Answer = sum(max(list(combinations(scores,k)),key = lambda x : x[0]+x[1]))
# print(Answer)
import sys
inf = sys.stdin 

T = inf.readline();

for t in range(0, int(T)):
    Answer=0;
    #############################################################################################
    from itertools import combinations
    k = int(inf.readline().split()[1])
    scores = []
    for i in inf.readline().split(): scores.append(int(i))
    Answer = sum(sorted(scores,reverse=True)[:k])
    #############################################################################################
    # Print the answer to standard output(screen).
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close()