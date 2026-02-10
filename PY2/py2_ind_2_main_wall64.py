"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 2 main
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

     

#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

import py2_ind_2_functions_wall64 as p
def main():
    name = input("Enter the name of the pool to calculate (Standard, Ramp, or Round): ")
    if (name == "Standard" or name == "Ramp" or name == "Round"):
        L1 = int(input("Enter the surface length or radius. "))
        L2 = int(input("Enter the surface width or bottom radius. "))
        Ds = int(input("Enter the shallow end depth. "))
        Dd = int(input("Enter the deep end depth. "))
        volume = 0
        if (name == "Standard"):
            volume = p.standard(L1,L2,Ds,Dd)
            if (volume != None):
                print(f"The volume of the {name} pool with your dimensions is {volume:,.2f} gallons.")  #77,552.46

        elif(name == "Round"):
            volume = p.round(L1,L2,Ds,Dd)
            if (volume != None):
                print(f"The volume of the {name} pool with your dimensions is {volume:,.2f} gallons.")  #77,552.46

        elif(name == "Ramp"):
            volume = p.ramp(L1,L2,Ds,Dd)
            if (volume != None):
                print(f"The volume of the {name} pool with your dimensions is {volume:,.2f} gallons.")  #77,552.46
            
    else:
        print("Please run the program again and enter a valid pool name.") 
        
    
            

if __name__ == "__main__":
    main()
