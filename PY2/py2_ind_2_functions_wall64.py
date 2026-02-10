"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 2
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
import math as m
     
C = (576/77) #Conversion from cubic feet to gallons
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

def standard(L1, L2, Ds, Dd):
    if ((L1<0) or (L2 < 0) or (Ds < 0) or (Dd < 0)):
        print("Please enter valid dimensions.")
        return None

    else:
        V = (Ds*L2*L1) + ((Dd - Ds)*(L1/3)*L2)
        G = V*C
        return(G)
    

def round(L1, L2, Ds, Dd):
    if ((L1<0) or (L2 < 0) or (Ds < 0) or (Dd < 0)):
        print("Please enter valid dimensions.")
        return None
    else:
        V = (m.pi*(m.pow(L1,2)*Ds)) + (1/3)*(m.pi)*(Dd-Ds)*(m.pow(L1,2) + m.pow(L2,2) + (L1*L2))
        G = V*C
        return(G)

def ramp(L1, L2, Ds, Dd):
    if ((L1<0) or (L2 < 0) or (Ds < 0) or (Dd < 0)):
        print("Please enter valid dimensions.")
        return None
    else:
        V = (((L1/3)*Ds*L2)/2) + ((L1/3)*Ds*L2) + ((L1/3)*Ds*L2) + ((L1/3)*(Dd-Ds)*L2)/2
        G = V*C
        return(G)




if __name__ == "__calc_volume__":
    calc_volume()
