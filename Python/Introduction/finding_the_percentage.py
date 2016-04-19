#!/usr/bin/env python
"""
You have a record of N students. Each record contains the student's name,
and their percent marks in Maths, Physics and Chemistry. The marks can be
floating values. The user enters some integer NN followed by the names and
marks for N students. You are required to save the record in a dictionary
data type. The user then enters a student's name. Output the average
percentage marks obtained by that student, correct to two decimal places.

Input Format
The first line contains the integer N, the number of students. The next
N lines contains the name and marks obtained by that student separated by a
space. The final line contains the name of a particular student previously
listed.

Output Format
Print one line: The average of the marks obtained by the particular student
correct to 2 decimal places.

Constraints
2 <= N <= 10
0 <= Marks <= 100

Sample Input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output
56.00

Concept
A dictionary is a data type which stores values in pairs. For each element in
the dictionary, there is a unique key that points to a value. A dictionary is
mutable. It can be changed.

For example:
>> a = {'one': 1} # Here 'one' is the key.
Note: The key of a dictionary is immutable. We cannot use a list as a key
because a list is mutable.

>> a['two'] = 2 # Adds key 'two' which points to 2
>> a['one']
1
>> if ('three' in a):
      # To check whether a certain string exist as a key in the dictionary
..    print a['three']
.. else:
..    print "Three not there"
Three not there
>> del a['one']
# Deletes index 'one' and the value associated with it
>> a
{'two': 2}

Note: A dictionary is unordered. So, only use the keys to navigate through the
dictionary.
"""
from __future__ import division, print_function


try:
    input = raw_input
except NameError:
    pass


def main():
    """Finding the percentage challenge."""
    number_of_students = int(input())
    students = {}
    for _ in range(number_of_students):
        input_string = input()
        input_list = input_string.split()
        students[input_list[0]] = input_list[1:]
    chosen_one = input()
    chosen_sum = sum(float(x) for x in students[chosen_one])
    chosen_average = round(chosen_sum / len(students[chosen_one]), 2)
    print("{0:.2f}".format(chosen_average))


if __name__ == '__main__':
    main()
