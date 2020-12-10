def solution(a, b):
    weekday = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    last_date = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    accumulated = b
    if a != 1:
        for i in range(1, a):
            accumulated += last_date[i]
    return weekday[(accumulated % 7)-1]

# Test
# a, b = 1, 1 # 'FRI'
# a, b = 1, 3 # 'SUN'
# a, b = 1, 13 # 'WED'
a, b = 2, 17 # WED
# a, b = 5, 24
print(solution(a, b))


