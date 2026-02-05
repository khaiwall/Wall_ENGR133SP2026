"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     12.1.2 Py2 Pre task 0 (for Python 1 Team task 1)
    Team ID:        LC1 - 03 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Khai, wall64@purdue.edu
    Date:           02/2/2026

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

import math as m


def calc_perform():
    a_string = input("Input a number for variable a: ")
    a = float(a_string)
    b = 135
    c = 3
    if (a > 4):

        value = (m.pow(a,2) + m.cos(b) - m.log(c)) / (b-(a*c))

    else:
        value = (m.sqrt(a+b)) / ((m.factorial(c)) + m.sin((b)))
    return value



def main():
    """Write your code here (and delete this line)."""
    value = calc_perform()
    v = round(value, 2)
    print("The result of the function was " + str(v))

if __name__ == "__main__":
    main()
#Comments go here WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW