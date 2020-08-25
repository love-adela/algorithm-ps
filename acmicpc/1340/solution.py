# boj.kr/1340
def is_leap_year(year:int)->bool:
    return True if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) else False

def get_number_of_dates(year:int, month:str)->int:
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
       return 31
    return 30 

monthly_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

month_str, date, year, strtime = input().split()
year = int(year)
month = monthly_dict[month_str] 
date = int(date.strip(','))
hour, minute = map(int, strtime.split(':'))
hour_to_minutes = hour*60+minute

total_minutes = 0
for m in range(1, 13):
    total_minutes += get_number_of_dates(year, m) * (24*60)

this_year_minutes = 0
for m in range(1, month):
    this_year_minutes += get_number_of_dates(year, m) * (24*60)

yesterday = date -1 
this_year_minutes += yesterday * (24*60)
this_year_minutes += hour_to_minutes

print((this_year_minutes / total_minutes) * 100)
