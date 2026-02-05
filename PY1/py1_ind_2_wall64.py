"""
Course Number: ENGR 13300
Semester: Spring 2026

Description:
  Will calculate the total capacatance of a capacator 

Assignment Information:
    Assignment:     py1 ind 2
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
    #userIn = 12.241421
    numUserIn = float(userIn)
    C1 = numUserIn
    C2= math.pow(math.e,3)*math.sqrt(5)
    STotalInverse = (1/C1) + (1/C2)
    STotal = round(1 / STotalInverse, 1)
    PTotal = round(C1 + C2,1)
    C1Answer = round(C1, 1)
    C2Answer = round(C2, 1)
    T = f"{'Type':<15}" f"{'First':<11}"f"{'Second':<12}"f"{'Total':>0}"
    S = f"{'Series':<8}"  f"{C1Answer:>9} \u03bcF" f"{C2Answer:>9} \u03bcF"  f"{STotal:>9} \u03bcF"
    P = f"{'Parallel':<0}"  f"{C1Answer:>9} \u03bcF" f"{C2Answer:>9} \u03bcF"  f"{PTotal:>9} \u03bcF"
    print(T)
    print(S)
    print(P) 

if __name__ == "__main__":
    main()


#random comment that has enough characters WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
"     "