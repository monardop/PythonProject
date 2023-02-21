"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""


def timeConversion(s):
    if 'AM' in s:
        hours = int(s[0:2])
        if hours == 12:
            return f"00{s[2:-2]}"
        else:
            return s[0:-2]
    else:
        hours = int(s[0:2])
        if hours == 12:
            return str(hours)+s[2:-2]
        else:
            hours += 12
            return str(hours)+s[2:-2]
            

timeConversion("07:30:43AM")
