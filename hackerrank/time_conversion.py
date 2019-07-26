import os
import sys
from datetime import datetime


def timeConversion(s):
    if not s.endswith("PM"):
        return s[:8]
    elif s.endswith("AM") and s.startwith("00"):
        return s[:8]
    else:
        return str(int(s[0:2]) + 12) + s[2:8]


def timeConversion1(s):
    my_date = datetime.strptime(s, '%I:%M:%S%p')
    return my_date.strftime("%H:%M:%S")


s = "12:05:39AM"
print(timeConversion(s))
print(timeConversion1(s))
