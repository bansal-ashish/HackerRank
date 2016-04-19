#!/usr/bin/env python
"""
Let's learn about Python's arithmetic operators.

First, let's read two integers:
a = int(raw_input())
b = int(raw_input())

The three basic arithmetic operators are the following:
Addition (+)
Subtraction (-)
Multiplication (*)
(We'll learn about division in the next task.)

Task
Read two integers from STDIN and print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Input Format
The first line contains the first integer, a. The second line contains the
second integer, b.

Constraints
1≤a≤10^10
1≤b≤10^10

Output Format
Print the three lines as explained above.

Sample Input
3
2

Sample Output
5
1
6

Explanation
3+2⟹5
3−2⟹1
3∗2⟹6
"""


from __future__ import print_function


def main():
    """Arithmetic Operators challenge."""
    first_int = int(raw_input())
    second_int = int(raw_input())
    print(first_int + second_int)
    print(first_int - second_int)
    print(first_int * second_int)


if __name__ == '__main__':
    main()
