#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    
    value = None
    
    # Starting col in the first middle value
    # first_col < col < last_col
    col = 1
    
    # Starting row in the first middle value
    # first_row < row < last_row
    row = 1
    
    last_col_n = len(arr[0])
    last_row_n = len(arr)
    
    # row-1,col-1  row-1,col    row-1,col+1
    #               row, col
    # row+1,col-1  row+1,col    row+1,col+1
    while row < (last_row_n - 1):
        while col < (last_col_n - 1):
            if value == None:
                value = arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1] + arr[row][col] + arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1]    
            else:
                new_sum = arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1] + arr[row][col] + arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1]
            
                if new_sum > value:
                    value = new_sum
            col += 1

        row += 1
        # Reset j to second col
        col = 1

    return value
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
