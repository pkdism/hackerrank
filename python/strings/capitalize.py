import math
import os
import random
import re
import sys

def solve(s):
    res = ''
    flag = False
    for i in range(len(s)):
        if i == 0:
            res += s[i].upper()
        elif (s[i] == ' '):
            res += s[i]
            flag = True
        elif flag == True:
            res += s[i].upper()
            flag = False
        else:
            res += s[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
