"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py3 ind 3
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

data = np.genfromtxt("Py3\list_of_features.csv", delimiter=",", dtype=str)


        # Map genotypes to phenotypes for each feature using nested dictionaries.
    # e.g., data_dict = {feature: {genotype: phenotype, ...}, ...}

    # data_dict = {
    #     "Head": {
    #         "SS": "Oval Shaped Head",
    #         "Ss": "Oval Shaped Head",
    #         "ss": "Round Shaped Head"
    #     },
    #     "Eye Color": {
    #         ...
    #     },
    #     ...
    # }

    # for row in data[1:, :]:
    #         data_dict = {}
    #         feature = None
    #         for row in data[1:, :]:
    #             feature = row[0] or feature
    #             genotype = row[3]
    #             phenotype = row[5]
    #             data_dict.setdefault(feature, {})
    #             data_dict[feature][genotype] = phenotype


def loop_find(type):
    for thing in data[0,:]:
        count=0
        if(thing == type):
            for thingo in data[:, count]:
                thin = thingo or None
                if (thin != thing and thin != None):
                    print(thingo)
        else:
            count+=1
            
def loop_through_feature(ftr):
    count = 1
    for thing in data[:,0]:
        if(thing == ftr):
            end = data[count,4]
            e = int(end)
            print(e)
            print("---")
            for i in range(count, count+e):
                print(data[count+i-1,3])
        count+=1
def main():
 
    again = "y"

    if (again == "y"):
        print("AVAILABLE FEATURES:")
        loop_find("Feature")
        print("----------------")
        feature = print("Please select feature: ___")
        feature = "Ear lobe"
        loop_through_feature(feature)


     

if __name__ == "__main__":
    main()
