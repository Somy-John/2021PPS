def solution(a, b):
    answer = ''
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    dates = [31,29,31,30,31,30,31,31,30,31,30,31]
    dateOfYear = sum(dates[:a-1])+b
    answer = day[dateOfYear%7-1]
    return answer