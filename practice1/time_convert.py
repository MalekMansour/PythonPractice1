'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
'''

def timeConversion(s):
    hours, minutes, seconds_am_pm = s.split(':')
    seconds, am_pm = seconds_am_pm[:2], seconds_am_pm[2:]

    if am_pm == 'PM' and hours != '12':
        hours = str(int(hours) + 12)
    elif am_pm == 'AM' and hours == '12':
        hours = '00'

    military_time = f"{hours}:{minutes}:{seconds}"
    return military_time

# Example:
time_12_hour_format = "07:45:32PM"
result = timeConversion(time_12_hour_format)
print(result)
