#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    bny = '{:032b}'.format(n)
    for i in range(len(bny)):
        if bny[i] == '0':
            bny = bny[:i] + '1' + bny[i+1:]
        elif bny[i] == '1':
            bny = bny[:i] + '0' + bny[i+1:]
    return int(bny, 2)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
