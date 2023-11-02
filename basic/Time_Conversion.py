#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[0:2])
    ampm = s[-2:]
    rest = s[2:-2]
    if hour == 12 and ampm == 'AM':
        return '00'+rest
    elif ampm == 'PM' and hour != 12:
        hour += 12
        return str(hour)+rest
    return s[:-2]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
