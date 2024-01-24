#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY days as parameter.
#

def solution(days):
    # Write your code here
    m = max(days)
    result = 0
    
    for i in days:
        if m != i:
            result = result +(m-i)
            
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):

        arr = list(map(int, input().rstrip().split()))

        ans = solution(arr)

        fptr.write(str(ans) + '\n')

    fptr.close()
