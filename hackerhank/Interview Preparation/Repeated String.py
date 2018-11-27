#!/bin/python3
#Challenge link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    string_size = len(s)
    s_quantity_of_a = s.count('a')

    n_full_string_repeated = n // string_size

    total_a = n_full_string_repeated * s_quantity_of_a

    # Get remaining as
    remaining_chars_qtd = n % string_size
    remaining_chars = s[:remaining_chars_qtd]
    remaining_a = remaining_chars.count('a')

    return total_a + remaining_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
