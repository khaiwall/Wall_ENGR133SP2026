"""
Course Number: ENGR 13300
Semester: Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     py3 pre 0
    Team ID:        LC1 - 03
    Author:         Khai, wall64@purdue.edu
    Date:           2/8/2026

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

""" Write any import statements here (and delete this line)."""

def build_matrix(rows, columns):
    
    my_matrix = []
    counter = 1
    for i in range(rows): 
        row = []
        for j in range(columns):
            column = [] 
            row.append(counter)
            counter += 1
        my_matrix.append(row)
    #print(my_matrix)
    return my_matrix

def traverse_with_for(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            value = m[i][j]
            print(f"X[{i},{j}] = {value}")

def traverse_with_while(m, stop):
    count = 1
    for i in range(len(m)):
            for j in range(len(m[i])):
                if (count < stop):
                    value = m[i][j]
                    print(f"X[{i},{j}] = {value}")
                    count+=1



def main():
    print("Enter Matrix Dimensions")
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))
    matrix = build_matrix(r,c)
    print("FOR loop traversal:")
    traverse_with_for(matrix)
    print("")
    print("Enter Matrix Dimensions")
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))
    s = int(input("Enter Stop Value: "))
    matrix = build_matrix(r,c)
    print("WHILE loop traversal:")
    traverse_with_while(matrix, s)

if __name__ == "__main__":
    main()

#11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111