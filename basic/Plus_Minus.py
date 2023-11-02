#Problem Description
#Print
#Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
#
#Input Format
#
#The first line contains an integer, n, the size of the array.
#The second line contains  space-separated integers that describe arr[n].

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    zero=0
    pos=0
    neg = 0
    for i in arr:
        if i == 0:
            zero+=1
        elif i > 0:
            pos+=1
        else:
            neg+=1
    print(pos/n)
    print(neg/n)
    print(zero/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
