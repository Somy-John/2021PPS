from itertools import combinations
n,m = int(input()), int(input())
rst = len(list(combinations(range(m-1),m-n)))
print(rst)