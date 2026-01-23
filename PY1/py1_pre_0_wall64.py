"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:    PythonPreTask00 
    Team ID:        LC001 Team 7
    Author:         Khai Wall, wall64@purdue.edu
    Date:           01/20/2026

Contributors:
    None

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
import math
""" Write any import statements here (and delete this line)."""


def main():

    a = 101
    b = 7
    c = 12.34
    """Write your code here (and delete this line)."""
    print(round((c**2) - math.pow(math.sin(b), 2), 3))
    print(round(math.factorial(b)*(math.cos(math.pi/c)-a), 3))
    print(round((c**((math.pi)*(math.e))*math.asin((math.sqrt(3))/2))/((a**(math.e))*b), 3))


if __name__ == "__main__":
    main()
