"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py3 ind 1
    Team ID:        LC1 - 03
    Author:         Khai, wall64@purdue.edu
    Date:           02/12/2026

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
import numpy as np

data = np.genfromtxt("list_of_features.csv", delimiter=",", dtype=str)


globalCount = 0

def loop_find(type):##prints all the things in one column
    for thing in data[0,:]:
        count=0
        if(thing == type):
            for thingo in data[:, count]:
                thin = thingo or None
                if (thin != thing and thin != None):
                    print(thingo)
        else:
            count+=1
            
def loop_through_feature(ftr):#loops through the features
    found = False
    count = 0
    for thing in data[:,0]:
        if(thing == ftr):
            print("POSSIBLE GENOTYPES:")
            found = True
            end = int((data[count,4]))
            e = end
            global globalCount
            globalCount = count
            global globalEnd
            globalEnd = e
            for i in range(count, count + e):
                print(data[i,3])
        count+=1
    if (found == False):
        print("Invalid feature.")
    return found


def geno_loop(gen):#loops through the genotype from the first to the last in a specific set of genotypes
    found = False
    global globalCount
    for thing in data[globalCount:(globalCount+globalEnd),3]:
        if(thing == gen):
            found = True
            phen = (data[globalCount,5])
            print(f"This corresponds to the physical attribute: {phen}")
        globalCount+=1
        
    if (found == False):
        print("Invalid genotype.")
    
    return found



def main():
    global globalCount
 
    again = "y"

    while (again == "y"):#while "again" is yes
        good = False
        while(good == False):
            print("AVAILABLE FEATURES:")
            loop_find("Feature")
            feature = input("Please select a feature: ")
            good = loop_through_feature(feature)
            if (good == True):
                geneotype = input("Please input the genotype: ")
                good = geno_loop(geneotype)
            good = True
        again = input("Would you like to run again (y or n)? ")


     #DKJF;LKDSAJFDSKJ;DSLAKJFDSA;LKFJDSA;LKJFD AD;LKJA DLKDSAJF SAFDKDSAFLKDSAFS FDS

if __name__ == "__main__":
    main()
