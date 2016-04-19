#!/usr/bin/env python
"""
Given an array of integers, calculate which fraction of its elements are
positive, which fraction of its elements are negative, and which fraction of
its elements are zeroes, respectively. Print the decimal value of each fraction
on a new line.

Note: This challenge introduces precision problems. The test cases are scaled
to six decimal places, though answers with absolute error of up to 10−410−4
are acceptable.

Input Format
The first line contains an integer, NN, denoting the size of the array.
The second line contains NN space-separated integers describing an array of
numbers (a0,a1,a2,…,an−1)(a0,a1,a2,…,an−1).

Output Format
You must print the following 3 lines:
 - A decimal representing of the fraction of positive numbers in the array.
 - A decimal representing of the fraction of negative numbers in the array.
 - A decimal representing of the fraction of zeroes in the array.

Sample Input
6
-4 3 -9 0 4 1

Sample Output
0.500000
0.333333
0.166667

Explanation
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The respective fractions of positive numbers, negative numbers and zeroes are
3/6=0.500000, 2/6=0.333333 and 1/6=0.166667, respectively.
"""
from __future__ import print_function, division


try:
    input = raw_input
except:
    pass


def fraction_of_positives(array):
    """Return fraction of positives in array."""
    positives = [x for x in array if x > 0]
    return len(positives) / len(array)


def fraction_of_negatives(array):
    """Return fraction of negatives in array."""
    negatives = [x for x in array if x < 0]
    return len(negatives) / len(array)


def fraction_of_zeros(array):
    """Return fraction of zeros in array."""
    zeros = [x for x in array if x == 0]
    return len(zeros) / len(array)


def plus_minus(array):
    """Print fractions of positives, negatives and zeros."""
    print(fraction_of_positives(array))
    print(fraction_of_negatives(array))
    print(fraction_of_zeros(array))


def main():
    """Program entry point."""
    input().strip()
    array = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    plus_minus(array)


if __name__ == '__main__':
    main()
