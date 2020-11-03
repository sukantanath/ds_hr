#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    row,col = 0,0
    max_sum = 0
    try:
        row = len(arr)
        col = len(arr[0])
    except:
        row = 0
        col = 0    
    
    if (row-2)*(col-2) < 0:
        return max_sum
    else:
        sum_list = []
        for r in range(row-2):
            for c in range(col-2):
                
                hg_sum = arr[r][c]+arr[r][c+1]+arr[r][c+2]+arr[r+1][c+1]+arr[r+2][c]+arr[r+2][c+1]+arr[r+2][c+2]
                sum_list.append(hg_sum)
        max_sum = max(sum_list)
        print(max_sum)
        
    return(max_sum)
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
