#!/usr/bin/env python
"""
Let's look at Python's input reading method.

>>> name = raw_input("Hey what's your name?\n")
Hey what's your name?
R2D2
>>> print name
R2D2

That's one way of doing it for yourself. However, we don't ask questions in
competitive programming, we answer them! We will only use raw_input() to read
a string without asking any questions to the system.

Task
Read a string from the console and print it.

Input Format
The first and only line of input contains a string.

Constraints
String length ≤ 500

Output Format
Print the same string back.

Sample Input
How many chickens does it take to cross the road?

Sample Output
How many chickens does it take to cross the road?
"""


from __future__ import print_function


def main():
    """Raw Input challenge."""
    input_string = raw_input()
    print(input_string)


if __name__ == '__main__':
    main()
