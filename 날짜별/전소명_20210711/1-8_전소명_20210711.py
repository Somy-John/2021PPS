from itertools import combinations
from math import sqrt

def solution(nums):
    answer = []
    numsCom = sorted(list(map(sum,list(combinations(nums,3)))))
    for currentNum in numsCom:
        n = int(sqrt(currentNum))
        for i in range(1,n+1):
            if currentNum%(i+1) == 0: break
        if(i==n): 
            answer.append(currentNum)
    return len(answer)