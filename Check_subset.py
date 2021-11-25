
#  - - - - - - - - - - - - - - - - - - Description of the Problem - - - - - - - - - - - - - - - - - - - - - - - #

"""
Challenge difficulty (given in the description on hackerrank.com) : Easy

You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input format:
The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

Output format:
Output True or False for each test case on separate lines.

Constraints:
- 0 < T < 21
- 0 < Number of elements in each set < 1001
"""

#  - - - - - - - - - - - - - - - - - - Code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# defining the function for the solution to be called for the lists
def solution(alis, blis):
    
    # storing the information about the length of the B set in a variable called "lenght_blis" (not needed, can be implemented into the code working with the length)
    length_blis = len(list(blis))
    
    # every element in set A gets added to set B, to find out, if A is a subset of B, by casting list B to a set which leads to erasion of duplicate values
    for i in alis:
        blis.append(i)
    blis = set(blis)
    
    # if the transformed set B's length is equal to the length of the list B, we know, that A is a strict subset of B -> print True 
    if len(list(blis)) == length_blis:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    
    # n = T
    n = int(input())
    
    # input gets read in
    for _ in range(n):
        a = int(input())
        alis = list(map(int, input().split()))
        b = int(input())
        blis = list(map(int, input().split()))
        
        # using our predefined function, so solve the problem for alis and blis
        solution(alis, blis)
        
        
        
