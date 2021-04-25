#There is a sequence of words in CamelCase as a string of letters,s , having the following properties:
#It is a concatenation of one or more words consisting of English letters.
#All letters in the first word are lowercase.
#For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
#Given s, determine the number of words in s.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    word_count = 0
    for i in range(len(s)):
        if s[i].isupper():
            word_count += 1
    return(word_count+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
