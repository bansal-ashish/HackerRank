#!/usr/bin/env python
"""
Your teacher has given you the task of drawing a staircase structure. Being an
expert programmer, you decided to make a program to draw it for you instead.
Given the required height, can you print a staircase as shown in the example?

Input
You are given an integer N depicting the height of the staircase.

Output
Print a staircase of height N that consists of # symbols and spaces. For
example for N=6, here's a staircase of that height:
     #
    ##
   ###
  ####
 #####
######
Note: The last line has 0 spaces before it.
"""
from __future__ import print_function


try:
    input = raw_input
except:
    pass


def print_staircase(number_of_steps):
    """Print staircase."""
    for step in range(number_of_steps):
        line = " " * (number_of_steps - (step + 1)) + "#" * (step + 1)
        print(line)


def main():
    """Program entry point."""
    number_of_steps = int(input().strip())
    print_staircase(number_of_steps)


if __name__ == '__main__':
    main()
