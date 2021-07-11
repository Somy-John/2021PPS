import itertools
from math import sqrt

def solution(nums):
    answer = []
    numsPer = list(map(sum,list(itertools.permutations(nums,3))))
    for currentNum in numsPer:
        n = int(sqrt(currentNum))
        print(n)
        for i in range(n):
            print(i)
            print(f'{currentNum}%{i+1} = {currentNum%(i+1)}')
            if currentNum%(i+1) == 0: break
        if(i==int(sqrt(currentNum))-1): 
            if currentNum not in answer: answer.append(currentNum)
    return len(answer)

solution([1,2,3,4])