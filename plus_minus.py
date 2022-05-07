'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers

Print
Print the ratios of positive, negative and zero values in the array.
Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, n , the size of the array.
The second line contains n space-separated integers that describe arr[n]
'''

import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive_numbers = 0
    negative_numbers = 0
    zero = 0
    size_arr = len(arr)

    for x in range(size_arr):
        if arr[x] > 0:
            positive_numbers += 1
        elif arr[x] < 0:
            negative_numbers += 1
        else:
            zero += 1

    print('%f' % (positive_numbers / size_arr))
    print('%f' % (negative_numbers / size_arr))
    print('%f' % (zero / size_arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
