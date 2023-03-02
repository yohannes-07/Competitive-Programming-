#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
   
    digits = sum(list(map(int, n)))
    p = str(digits) * int(k)
 
    def helper(p):
        if len(p) == 1:
            return int(p)
        
        ps = list(map(int, p))
        
        super_digit = sum(ps)
        return helper(str(super_digit))
    
    ans = helper(p)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
