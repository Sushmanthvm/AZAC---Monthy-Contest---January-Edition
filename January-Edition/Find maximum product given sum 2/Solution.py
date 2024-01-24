#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER S as parameter.
#

def solution(S):
    # Write your code here
    if S > 0:
        return -(S+1)
        
        
    elif S < 0:
        return S-1
        
    else:
        return -1
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        S = int(input().strip())

        ans = solution(S)

        fptr.write(str(ans) + '\n')

    fptr.close()
