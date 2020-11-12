#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    val = 0
    max_val = 0
    master_max = [0]*n
    
    for i in range(len(queries)):
        start_pos = queries[i][0] - 1
        end_pos = queries[i][1] 
        if start_pos >= 0:
            master_max[start_pos] += queries[i][2]
        if end_pos < n:
            master_max[end_pos] -= queries[i][2]
            
    print([k for k in master_max])
    
    for j in range(len(master_max)):
        
        val += master_max[j]
        #master_max[j] += master_max[j-1]
        if val > max_val:
            max_val = val
                        
    
    print(max_val)
    
    return (max_val)
        
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
