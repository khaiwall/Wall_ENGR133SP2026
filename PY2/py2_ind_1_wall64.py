"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 1
    Team ID:        LC1 - 03
    Author:         Khai, wall64@purdue.edu
    Date:           e.g. 01/23/2026

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


def check_status(T, P):
    Tmax = 344.14
    TmaxPcnt = 344.14*0.95
    Tmin = 304.2
    Pmax = 137
    PmaxPcnt = 137*0.95
    Pmin = 73.8

    if (T>Tmin and T<TmaxPcnt):
        print("Temperature is within safe operating conditions.")
    if (T >= TmaxPcnt):
        newT = T - TmaxPcnt
        print("Warning! Reduce the temperature!")
        print("Decrease the temperature by at least", f"{newT:.2f}", "Kelvin.")
    if (T < Tmin):
        Tinc = Tmin - T
        print("CO2 is below the critical temperature.")
        print("Increase the temperature by at least",f"{Tinc:.2f}", "Kelvin.")    
    if (P >= PmaxPcnt):
        newP = P - PmaxPcnt
        print("Warning! Reduce the pressure!")
        print("Decrease the pressure by at least", f"{newP:.2f}", "bar.")
    if (P>Pmin and P<PmaxPcnt):
        print("Pressure is within safe operating conditions.")
    if (P == Pmin and T == Tmin):
        print("CO2 is at the critical point.")
    if (P < Pmin):
        Pinc = Pmin - P
        print("CO2 is below the critical pressure.")
        print("Increase the pressure by at least",f"{Pinc:.2f}", "bar.")
    


     

#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

def main():
    T = float(input("Enter the temperature of carbon dioxide in Kelvin: " ))
    if (T>0):
        P = float(input("Enter the pressure of carbon dioxide in bar: "))
        if (P>0):
            check_status(T,P)
        else:
            print("Error: Please enter a valid pressure.")

    else:
        print("Error: Please enter a valid temperature.")
        


if __name__ == "__main__":
    main()
