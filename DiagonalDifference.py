'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute diference is
15 - 17 = 2.

Function description
Complete the diagonalDifference function in the editor below.
diagonalDifference takes the following parameter:
int arr[n][m]: an array of integers

Return
int: the absolute diagonal difference

Input Format
The first line contains a single integer, n, the number of rows and columns in the square matrix ar.
Each of the next n lines describes a row, arr il, and consists of n space-separated integers arr 2 .

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

'''

import math
import os
import random
import re
import sys



def diagonalDifference(arr):
    # Write your code here
    first_diagonal = 0
    second_diagonal = 0
    tam_matrix = len(arr)

    for x in range(tam_matrix):
        first_diagonal += arr[x][x]

    for y in range(tam_matrix):
        second_diagonal += arr[y][(tam_matrix) - 1 - y]

    absolute_difference = abs(first_diagonal - second_diagonal)
    return absolute_difference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
