

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

# defining the solution-function
def main():
    
    # n is not import for solving the challenge but to input the sample
    n = int(input())
    # defining lists for solution
    nest_list = []
    score_l = []
    
    # appending the name and the score of each student to our list
    for _ in range(n):
        name = input()
        score = input()
        nest_list.append([score, name])
        
    # appending the individual scores to an extra list to check for the second lowest values
    for i in nest_list:
        score_l.append(float(i[0]))
        
    # duplicates will be deleted by changing the list to a set, because sets do not allow duplicate values
    score_l = set(score_l)
    # formatted set gets changed to list for easier handling and the use of ".sort()"
    score_l = list(score_l)
    # the score list gets sorted to evaluate the second lowest grade
    score_l.sort()
    
    # defining a list which will hold the names of the students having the second lowest grade
    sec_low = []
    
    # searching the nest_list for the student names that are connected to the second lowest score
    for i in nest_list:
        # float(i[0]) represents the score connected to a students name (Note that the nest_list is of shape (score, name))
        # float(score_l[1]) represents the second lowest number in our score list, which holds the score values individually for easier handling
        if float(i[0]) == float(score_l[1]):
            sec_low.append(i[1])
    
    # sorting the list of students with the second lowest grade alphabetically
    sec_low.sort()
    
    # printing the names
    for j in sec_low:
        print(j)
        
if __name__ == "__main__":
    main()
