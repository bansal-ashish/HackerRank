#!/usr/bin/env python
"""
In Python 2, the default print is a simple IO method that doesn't give many
options to play around with.

The following two examples will summarize it.

Example 1:
var, var1, var2 = 1,2,3
print var
print var1, var2
Prints two lines and, in the second line, var1var1 and var2var2 are separated
by a single space.

Example 2:
for i in xrange(10):
    print i,
Prints each element separated by space on a single line. Removing the comma at
the end will print each element on a new line.

Let's import the advanced print_function from the __future__ module.

Its method signature is below:
print(value, ..., sep=' ', end='\n', file=sys.stdout)
Here, you can add values separated by a comma. The arguments sep, end, and
file are optional, but they can prove helpful in formatting output without
taking help from a string module.

The argument definitions are below:
 - sep defines the delimiter between the values.
 - end defines what to print after the values.
 - file defines the output stream.

Interesting, isn't it?

Task
Read an integer N.

Without using any string methods, try to print the following:

1,2,3.....N

Note that "....." represents the values in between.

Input Format
The first line contains an integer NN.

Output Format
Output the answer as explained in the task.

Sample Input
3

Sample Output
123

Pro Tip
You can use the print function inside a map(). Can you do a 1 line code to
solve the problem above?

Yes I can!
For Python3:
>>>print(*range(1, int(input()) + 1), end='', sep='')
"""
from __future__ import print_function


try:
    input = raw_input
except NameError:
    pass


def main():
    """Print Function challenge."""
    n = int(input())
    for i in range(n):
        print(i + 1, sep='', end='')


if __name__ == '__main__':
    main()
