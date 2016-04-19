#!/usr/bin/env python
"""
Let's learn the basics of Python! You are given the first and last name of a
person. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
It's that simple!

In Python, you can read a line as a string using:

s = raw_input()
#here s reads the whole line.
Input Format
The first line contains the first name, and the second line contains the last
name.

Constraints
The length of the first and last name ≤ 1010.

Output Format
Print the output as mentioned above.

Sample Input

Guido
Rossum
Sample Output

Hello Guido Rossum! You just delved into python.
Concept
The input read by the program is stored as a string data type. A string is a
collection of characters.
"""
from __future__ import print_function


try:
    input = raw_input
except NameError:
    pass


def main():
    """What's Your Name challenge."""
    first_name = input()
    second_name = input()
    greetings = "Hello {} {}! You just delved into python."
    print(greetings.format(first_name,second_name))


if __name__ == '__main__':
    main()
