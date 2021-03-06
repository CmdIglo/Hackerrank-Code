
#  - - - - - - - - - - - - - - - - - - Description of the Problem - - - - - - - - - - - - - - - - - - - - - - - #

"""
Challenge difficulty (given in the description on hackerrank.com) : Medium

Consider the following:

- A string, s, of length n where s=c0c1...cn-1.
- An integer, k, where k is a factor of n.

We can split s into n/k substrings where each substring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

- The characters in ui are a subsequence of the characters in ti.
- Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti 
occurs at a previous index <j in ti, then do not include the character in string ui.

Given s and k, print n/k lines where each line i denotes string ui.

Input format:
The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.

Constraints:
- 1 <= n <= 10^4, where n is the lenght of s
- 1 <= k <= n
- it is guaranteed that n is a multiple of k
"""

#  - - - - - - - - - - - - - - - - - - Code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# the function has to have two arguments: string and k (see description above)
def merge_the_tools(string, k):
    
    # Input string gets formatted into list to create substrings 
    strlist = [i for i in string]
    # list of substrings with the length of k
    chunks = [strlist[x:x+k] for x in range(0, len(strlist), k)]
    
    # deleting duplicates in the substrings (can also be done by formatting the list to sets and back) and replacing substrings by the new substrings
    for i in range(len(chunks)):
        
        lis = []
        
        # checks if each value j is already in the list "lis", if not append, if yes skip
        for j in chunks[i]:
            if j not in lis:
                lis.append(j)
        
        # the substring gets replaced by the list which we created by leaving out duplicate values
        chunks[i] = lis
    
    # printing the substrings as strings
    for i in range(len(chunks)):
        print("".join(letter for letter in chunks[i]))
