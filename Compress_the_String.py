
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

# The challenge was about the itertools.groupby() function. It takes an iterable as an argument and returns the consecutive occurences 
# of a value in the iterable along with the value itself i.e.: [1, 1, 2, 3, 3, 3, 4, 4] => (1, 2) (2, 1) (3, 3) (4, 2)
from itertools import groupby

def main():
    
    # input as a string, for example "111133426666"
    n = input()
    # formatting the string into an iterable i.e. list
    nLis = [i for i in n]
    
    # for every value in nLis it's occurences and the value itself gets returned and printed in the format : (occurences, value)
    # Note that the value mentioned above is "key" in this example and the number of occurences is value (len(value))
    for key, value in groupby(nLis):
        print("({}, {})".format(len(list(value)), key), end=" ")
        
if __name__ == "__main__":
    main()
