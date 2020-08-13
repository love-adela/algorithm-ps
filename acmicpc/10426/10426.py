def is_leap_year(y:int)->bool:
    return (y % 4 == 0 and y % 100 !=0) or y % 400 == 0

def get_last_date(y:int, m:int)->int:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31 
    elif m == 2:
        return 29 if is_leap_year(y) else 28 
    return 30 

def is_date_overflow(year:int, month:int, date:int)->bool:
    return date > get_last_date(year, month)
    
date_str, delta_days = input().split()
year, month, date = map(int, date_str.split('-'))

date += int(delta_days) -1

while is_date_overflow(year, month, date):
    date -= get_last_date(year, month)
    month += 1
    if month > 12:
        month -= 12
        year += 1

print(f'{year}-{month:02}-{date:02}')
