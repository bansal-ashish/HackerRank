#!/usr/bin/env python2
"""
Loops are control structures that iterate over a range to perform a certain
task.

There are two kinds of loops in Python.

A for loop:

for i in range(0,5):
    print i
And a while loop:

i = 0
while i < 5:
    print i
    i+=1
Here, the term range(0,5) returns a list of integers from 0 to 5:
[0,1,2,3,4].

Task
Read an integer N. For all non-negative integers i<N, print i^2. See the
sample for details.

Input Format
The first and only line contains the integer, N.

Constraints
1≤N≤20

Output Format
Print N lines, one corresponding to each i.

Sample Input
5

Sample Output
0
1
4
9
16
"""


from __future__ import print_function


def main():
    """Loops challenge."""
    loop_len = int(raw_input())
    for i in range(loop_len):
        print(i ** 2)


if __name__ == '__main__':
    main()
