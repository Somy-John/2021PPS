def solution(skill, skill_trees):
    answer = 0
    prio = {}
    for i in range(len(skill)):
        prio[skill[i]] = i
    key = list(prio.keys())
    for j in range(len(skill_trees)):
        check = []
        for k in skill_trees[j]:
            if k in key:
                check.append(k)
        if all(check[l] == key[l] for l in range(len(check))):
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CXF", "ASF", "BDF", "CEFD"]))
