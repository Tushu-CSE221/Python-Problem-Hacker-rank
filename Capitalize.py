
import math
import os
import random
import re
import sys

def solve(s):
    # Iterate through each character in the string while respecting spaces
    result = ' '.join(word.capitalize() for word in s.split(' '))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
