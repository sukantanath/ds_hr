#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    for char in a:
        res_a = a.find(char)
        res_b = b.find(char)
        
        if res_b > -1:
            print(char,res_a,res_b)
            if res_a < len(a)-1:
                a = a[:res_a]+a[res_a+1:]
            elif res_a == len(a)-1:
                a = a[:res_a]
            if res_b < len(b)-1:
               b = b[:res_b]+b[res_b+1:]
            elif res_b == len(b)-1:
                b = b[:res_b]
            #print(a,b)
    print(len(a)+len(b))
    return(len(a)+len(b))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
