"""
Course Number: ENGR 13300
Semester: Spring 2026

Description:
    We need to evaluate the integral from a to b of sin(x)/x, which does not have an elementary anti-derivative. Instead, we are using the Mclaren series which allow us to approximate the value of sin(x)/x, and then using a summation to act as an integral

Assignment Information:
    Assignment:     py3 ind 2
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
    d = int(input("Enter the number of decimal places for convergence: "))
    n = int(input("Enter the maximum number of terms: "))
    print("")
    print("Approximations:")
    si = 0.0
    newSi = 0.0
    count = 0
    endPoint = 0


    if (n > 0 and d > 0): ##checking if input values are valid
        for i in range(n):
            newSi = si #Here we are storing the "old value" of the summation which we will compare to the new value later
            if (count < 2): #if the decimals have matched enough times (count is great enough) then we will not evaluate the sum
               
                si += ((-1)**i)*(((b**(2*i+1)) - (a**(2*i+1))) / ((2*i+1)*m.factorial(2*i+1)))
                print(f"n = {i}: sum = {round(si,d)}")
                endPoint+=1
            if (round(newSi,d) == round(si,d)): ##here we are comparing the old and new values. If they are equal (the decimals are the same) then we add 1 to count.
                count+=1
               

        if (count < 2):
            print(f"Error: The approximation did not converge to {d} decimal places with only {n} terms.")
        else:
            print(f"The integral from {a} to {b} is estimated to be {si:.{d}f}.")
            print(f"Total number of terms: {endPoint}")
            

    else:
        print("Error: Input a positive integer")


if __name__ == "__main__":
    main()
#you need 133 characters of comments? I gotchu...