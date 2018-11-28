#!/bin/python3
#Challenge link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    safe_clouds = [pos for pos, cloud in enumerate(c) if cloud == 0]
    #print(safe_clouds)
    jumps_array = list()

    # Indice inicial constante
    cloud_index = 0
    while cloud_index < len(c)-1:
        # Every time I have my actual index inside my safe_clouds list I append my c
        # respective value of that index in my jumps array
        # How the max possibility of clound jump is two. We first check if the index            # of the cloud two jumps ahead is safe. If it's not we just jump one cloud.
        # We always will jump one or two clouds.
        if cloud_index + 2 in safe_clouds:
            jumps_array.append(c[cloud_index + 2])
            cloud_index = cloud_index + 2
        else:
            jumps_array.append(c[cloud_index + 1])
            cloud_index = cloud_index + 1

    return len(jumps_array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
