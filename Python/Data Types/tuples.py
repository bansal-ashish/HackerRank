#!/usr/bin/env python
"""
Task
You are given an integer, N, on a single line. The next line contains N
space-separated integers. Create a tuple, T, of those N integers, then compute
and print the result of hash(T).
Note: hash() is one of the functions in the __builtins__ module.

Input Format
The first line contains an integer, N (the number of elements in the tuple).
The second line contains NN space-separated integers describing T.

Output Format
Print the result of hash(T).

Sample Input
2
1 2

Sample Output
3713081631934410656
"""

from __future__ import print_function, unicode_literals


try:
    input = raw_input
except NameError:
    pass


def main():
    number_of_items = int(input().strip())
    user_input = input().split()
    user_tuple = tuple([int(x) for x in user_input])
    print(hash(user_tuple))


if __name__ == '__main__':
    main()
