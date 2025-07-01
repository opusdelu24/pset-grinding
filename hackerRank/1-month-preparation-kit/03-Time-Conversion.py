#import math
#import os 
#import random 
#import re
#import sys

#planning:
# in-> String ->rule-> number -> compute -> number -> String

# format hh:mm:ss:--
# 1 am midnight 1
# 3 am midnight 3
# 3 pm lunch time
# get time 
# check AM or PM
# if AM
## 1 -> 1
## use that number before 12 (lunch)
# elif PM
## 1 -> 13, 12 -> 24
## hh + 12

time_normal = str()
#01:34:6789
if time_normal[8] == 'A':
    return time_normal[0:8] # have to check first
else:
    new_time = str(int(time_normal[0:2])+ 12) 
    new_time = new_time + time_normal[2:8]
    return new_time

"""
def timeConversion(s):
    if s[8] == 'A':
        return s[0:8]
    else:
        new_time = str(int(s[0:2])+12)
        new_time = new_time + s[2:8]
        return new_time

wrong half of test cases
"""
