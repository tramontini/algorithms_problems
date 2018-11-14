#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # n = number of socks
    # ar = colors
    # socks = dictionary with the quantity of each colors
    socks = {}
    
    for number in ar:
        if number in socks.keys():
            socks[number] += 1
        else:
            socks[number] = 1
        
    pair_quantity = 0
    for sock in socks.values():
        pairs = int(sock/2)
        pair_quantity += pairs
    
    return pair_quantity

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
