'''
Function Description

Complete the staircase function in the editor below.

staircase has the following parameter(s):

int n: an integer
Print

Print a staircase as described above.

Input Format

A single integer, , denoting the size of the staircase.
'''

import math
import os
import random
import re
import sys

def staircase(n):
    for x in range(n):
        for y in range(n):
            if x + y >= n-1:
                print('#', end='')
            else:
                print(' ', end='')
        print('\r')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)