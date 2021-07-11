from itertools import combinations, permutations
def solution(number, k):
    rst = []
    for indexes in list(combinations(range(len(number)),k)):
        tmp = number
        for j in range(len(indexes)):
            tmp = tmp[0:indexes[j]-j]+tmp[indexes[j]-j+1:]
        rst.append(int(tmp))
    return max(rst)

print(solution("1924",2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
