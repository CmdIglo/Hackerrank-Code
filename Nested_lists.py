

#  - - - - - - - - - - - - - - - - - - Description of the Problem - - - - - - - - - - - - - - - - - - - - - - - #

"""
Challenge difficulty (given in the description on hackerrank.com) : Easy

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Input format:
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Output format:
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Constraints:
- 2 <= N <= 5
- There will always be one or more students having the second lowest grade.
"""

#  - - - - - - - - - - - - - - - - - - Code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

def main():
    n = int(input())
    nest_list = []
    score_l = []
    
    for _ in range(n):
        name = input()
        score = input()
        nest_list.append([score, name])
        
    for i in nest_list:
        score_l.append(float(i[0]))
        
    score_l = set(score_l)
    score_l = list(score_l)
    score_l.sort()
    
    sec_low = []
    
    for i in nest_list:
        if float(i[0]) == float(score_l[1]):
            sec_low.append(i[1])
            
    sec_low.sort()
    
    for j in sec_low:
        print(j)
        
if __name__ == "__main__":
    main()
