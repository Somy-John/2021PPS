from datetime import datetime, timedelta
def dayOfYear(date):
    date = list(map(int,date.split("-")))
    return (datetime(date[0],date[1],date[2])-datetime(date[0], 1, 1)).days+1
    
print(dayOfYear("2019-01-09"))