"""
Course Number: ENGR 13300
Semester: Spring 2026

Description:
  Will calculate the total capacatance of a capacator 

Assignment Information:
    Assignment:     Python01 Individual Task 2
    Team ID:        001
    Author:         Khai Wall wall64@purdue.edu
    Date:           1/25/2026

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


import math

def main():
    
    userIn = input("Input the capacitance of the first capacitor [\u03bcF]: ")
    C1 = int(userIn)
    print("c is: " + str(C1))
    T = ["Type", "First", "Second", "Total"]
    C2String = f"{math.pow(math.e,3)*math.sqrt(5):5.1f}"
    C2 = float(C2String)
    STotalInverse = (1/C1) + (1/C2)
    STotal = 1 / STotalInverse
    PTotal = C1 + C2
    S = ["Series", f"{C1:5.1f}", f"{C2:5.1f}", f"{STotal:5.1f}"]
    P = ["Parallel", f"{C1:5.1f}", f"{C2:5.1f}", f"{PTotal:5.1f}"]
    print(T)
    print(S)
    print(P)
    

if __name__ == "__main__":
    main()
