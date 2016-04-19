#!/usr/bin/env python
"""
Given a time in AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a
24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00
on a 24-hour clock.

Input Format
A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or
hh:mm:ssPM), where 01≤hh≤12.

Output Format
Convert and print the given time in 2424-hour format, where 00≤hh≤2300≤hh≤23.

Sample Input
07:05:45PM

Sample Output
19:05:45
"""
from __future__ import print_function


try:
    input = raw_input
except:
    pass


def convert_time(time):
    """Convert time from AM/PM format to 24-hour format."""
    period = time[-2:]
    hours = int(time.split(':')[0])
    if period == 'AM':
        if hours == 12:
            hours = 0
        return str(hours).zfill(2) + time[2:-2]
    elif period == 'PM':
        if hours != 12:
            hours += 12
        return str(hours).zfill(2) + time[2:-2]


def main():
    """Program entry point."""
    time = input().strip()
    print(convert_time(time))


if __name__ == '__main__':
    main()
