"""
Course Number: ENGR 13300
Semester: Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py ind 2
    Team ID:        LC1 - 03 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Khai, wall4@purdue.edu
    Date:           2/10/2026 

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
import numpy as np

def main():
    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))
    d = int``(input("Enter the number of decimal places for convergence: "))
    n = int(input("Enter the maximum number of terms: "))

    si = 0.0

    if n > 0:
        for i in range(n):
            si += ((-1**i)*(b**(2*i+1)) - (a**(2*i+1)))/ ((2*i+1)*m.factorial(2*i+1))
            print(f"n = {i}: sum = {si:.{d}f}") 



    """Write your code here (and delete this line)."""


if __name__ == "__main__":
    main()
