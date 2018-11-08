#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    sea_level = 0
    valleys = 0
    step_num = 0
    s = list(s[0])

    for step in s:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1

        if sea_level == -1 and s[step_num+1] == 'U':
            valleys += 1

        step_num += 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
