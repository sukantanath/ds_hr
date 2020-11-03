#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    size = 0
    min_bribe = 0
    curr_pos = 0

    try:
        size = len(q)
    except:
        size = 0
    
    for i in range(size):
        curr_pos = q[i]
        #print(i,curr_pos)
        if (curr_pos - (i +1)) > 2:
            print("Too chaotic")
            return 
        else:
            #if(i+1 < size and curr_pos > q[i+1]):
            
            for j in range(max(0,curr_pos-2),i):
                if q[j] > curr_pos:
                    min_bribe += 1
                #min_bribe = min_bribe+ curr_pos - (i+1)
                    #print("In else: ",min_bribe)
    
    print(min_bribe)
    return 
    
if __name__ == '__main__':
    t = int(input())
