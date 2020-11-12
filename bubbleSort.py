#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swapCount = 0
    
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped = True
                swapCount +=1
        if swapped == False:
            break
    print("Array is sorted in",swapCount,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[n-1])       
                
                
        
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
