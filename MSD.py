#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def solution(s):
    # Write your code here
    sum =0
    for i in s:
        sum = sum + ord(i)
    
    if sum%7 == 0:
        return "THALA FOR A REASON"
    else:
        return "IAM SAD"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        ans = solution(s)

        fptr.write(ans + '\n')

    fptr.close()
