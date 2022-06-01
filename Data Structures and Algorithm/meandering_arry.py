#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'meanderingArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY unsorted as parameter.
#

def meanderingArray(unsorted):
    srted = unsorted.sort()
    print(srted)
    return srted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    unsorted_count = int(input().strip())

    unsorted = []

    for _ in range(unsorted_count):
        unsorted_item = int(input().strip())
        unsorted.append(unsorted_item)

    result = meanderingArray(unsorted)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
