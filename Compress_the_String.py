
#  - - - - - - - - - - - - - - - - - - Description of the Problem - - - - - - - - - - - - - - - - - - - - - - - #

"""
Challenge difficulty (given in the description on hackerrank.com) : Medium

You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

Input format:
A single line of input consisting of the string S.

Output format:
A single line of output consisting of the modified string.

Constraints:
All the characters of S denote integers between 0 and 9.
0 < S < 10^4
"""

#  - - - - - - - - - - - - - - - - - - Code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

from itertools import groupby

def main():
    n = input()
    nLis = [i for i in n]
    for key, value in groupby(nLis):
        print("({}, {})".format(len(list(value)), key), end=" ")
        
if __name__ == "__main__":
    main()
