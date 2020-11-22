#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    change_cnt = 0
    cnt = 0
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char,0)+1

    c = Counter(Counter(s).values())
    print(c)
    print(c.values())
    if len(c)==1:
        return "YES"
    if len(c)>2:
        return "NO"
    if  1 in c.values() and (c[min(c.keys())]==1 or (max(c.keys()) - min(c.keys())==1)):
        return "YES"
    else:
        return "NO"
    # for val in char_dict.values():
    #     if cnt == 0:
    #         cnt = val
    #         continue
    #     elif (abs(cnt-val) >= 2):
    #         return "NO"
    #     else:
    #         change_cnt += abs(cnt-val)
    #         if change_cnt > 1:
    #             return "NO"
    #     #cnt = val
    
    # return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
