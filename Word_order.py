
#  - - - - - - - - - - - - - - - - - - Description of the Problem - - - - - - - - - - - - - - - - - - - - - - - #

"""
Challenge difficulty (given in the description on hackerrank.com) : Medium

You are given n words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Input format:
The first line contains the integer, n.
The next n lines each contain a word.

Output format:
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Constraints:
- 1 <= n <= 10^5
- The sum of the lengths of all the words do not exceed 10^6.
- All the words are composed of lowercase English letters only.
"""

#  - - - - - - - - - - - - - - - - - - Code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

def main():
    # n denotes the number of follwoing lines containing a word
    n = int(input())
    
    # defining a dictionary to assign each word a number of occurences
    dict = {
        
    }
    
    # for the following n lines of input the code checks if the word is already in the dictionary if yes then 1 gets added to the assigned value of the word
    # in the dictionary if not the value 1 gets assigned to the word
    for _ in range(n):
        st = input()
        if st in dict.keys():
            dict[st] += 1
        else:
            dict[st] = 1
    
    # printing the solution: first print how many distinct words are in the dictionary then print the numbers of occurences according to their appearance int
    # the input
    print(len(dict))
    for i in dict.values():
        print(i, end =" ")

if __name__ == "__main__":
    main()
