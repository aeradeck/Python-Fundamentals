"""
Math and Variables Lab
By: FIXME
CSCI 110 Lab
Date: FIXME
 
Read and solve: Add Two Numbers - https://open.kattis.com/problems/addtwonumbers 
 
Algorithm steps:
  1. Read data as a line
  2. Split the line into two integers
  3. Add them up
  4. print the result
"""

import sys


def main():
    """Main function that solves the problem
    """

    # FIXME1 - read input data into a variable #fixed#
    line = input()
    # split the data into two numbers
    a, b = line.split()
    # check to see if the data is split correctly
    print(f'{a=}, {b=}', file=sys.stderr)
    # Fixed 2: convert string a into integer
    a = int(a)
    # Fixed 3: convert string b into integer
    b = int(b)
    # Fixed 4: add two numbers and store the result into ans variable
    ans =a+b
    # Fixed 5: print the answer as shown in the sample output
    print(ans)

main()  # call main function
