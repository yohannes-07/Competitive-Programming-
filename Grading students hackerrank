#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    modifiedGrades = []
    for i in grades:
        if len(grades) > 60 or i > 100:
            print("the number of students should be <60 and the grade be < 100")
            break
        else:
            if i < 38:
                modifiedGrades.append(i) 
            else:
                for j in range(i):
                    if j*5 > i:
                        x = j*5
                        break
                    
                if x - i >= 3:
                     modifiedGrades.append(i) 
                else:
                     modifiedGrades.append(x)
    return modifiedGrades 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
