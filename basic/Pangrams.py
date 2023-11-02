#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(alphabet)):
        yn = False
        for j in range(len(s)):
            if alphabet[i] == s[j]:
                yn = True
        if yn is False:
            return 'not pangram'
    return 'pangram'
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
