#!/usr/bin/env python
"""
Given a square matrix of size N×N, calculate the absolute difference between
the sums of its diagonals.

Input Format
The first line contains a single integer, NN. The next NN lines denote the
matrix's rows, with each line containing NN space-separated integers describing
the columns.

Output Format
Print the absolute difference between the two sums of the matrix's diagonals
as a single integer.

Sample Input
3
11 2 4
4 5 6
10 8 -12

Sample Output
15

Explanation
The primary diagonal is:
11
      5
            -12
Sum across the primary diagonal: 11 + 5 - 12 = 4
The secondary diagonal is:
            4
      5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15
"""
from __future__ import print_function


try:
    input = raw_input
except:
    pass


def diagonal_difference(matrix_size, matrix):
    """Calculate diagonal difference of an matrix."""
    prime_diag_sum = 0
    secondary_diag_sum = 0
    for i in range(matrix_size):
        prime_diag_sum += matrix[i][i]
        secondary_diag_sum += matrix[i][matrix_size - 1 - i]
    return abs(prime_diag_sum - secondary_diag_sum)


def main():
    """Program entry point."""
    matrix_size = int(input().strip())
    matrix = []
    for _ in range(matrix_size):
        matrix_line = [int(a_temp) for a_temp in input().strip().split(' ')]
        matrix.append(matrix_line)
    print(diagonal_difference(matrix_size, matrix))


if __name__ == '__main__':
    main()
