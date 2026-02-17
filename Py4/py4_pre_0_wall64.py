"""
Course Number: ENGR 13300
Semester: Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     py4 pre 0
    Team ID:        LC1 - 03 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Khai, wall64@purdue.edu
    Date:           02/14/2026

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

import pandas as p
import matplotlib.pyplot as plt
def main():
    

    # df = p.read_csv("Py4\py4_pre_0_data.csv", header=None)
    df = p.read_csv("py4_pre_0_data.csv", header=None)

    df_Volume = p.DataFrame()
    df_Volume[0] = df[0]
    df_Volume[1] = round((df[1] * df[2]) + 0.01, 1) ##ensures it matches the formatting
    
    
    df_Volume.to_csv("py4_pre_0_wall64.csv", index = False, header = False)


    fig, ax = plt.subplots(1,2)
    fig.suptitle("Financial Data Analysis")
    ax[0].plot(df[0],df[2], 'bo-', label='Price')
    ax[0].grid()
    ax[0].legend()
    ax[0].set_title("Stock Price vs Time")
    ax[0].set_xlabel("Time (days)")
    ax[0].set_ylabel("Price (USD)")
    
    
    ax[1].bar(df_Volume[0],df_Volume[1],color = 'red', label = 'Dollar Volume')
    ax[1].grid()
    ax[1].set_ylim(0, 3000)
    ax[1].set_title("Dollar Volume vs Time")
    ax[1].set_xlabel("Time (days)")
    ax[1].set_ylabel("Volume (USD)")
    ax[1].legend()
 
    fig.tight_layout()
    plt.show(block=True)

    # plt.subplot(1,2,1)
    
    # plt.plot(df[0], df[2], 'bo-', label='Price')
    # plt.title("Stock Price vs Time")
    # plt.legend()
    # plt.grid()
    # plt.xlabel("Time (days)")
    # plt.ylabel("Price (USD)")
    
    # plt.subplot(1,2,2)
    # plt.bar(df_Volume[0], df_Volume[1], color = 'red', label ='Dollar Volume')
    # plt.ylim(0, 3000)
    # plt.title("Dollar Volume vs Time")
    # plt.legend()
    # plt.grid()
    # plt.xlabel("Time (days)")
    # plt.ylabel("Volume (USD)")
    # plt.tight_layout()
    # plt.show()

    """Write your code here (and delete this line)."""


if __name__ == "__main__":
    main()
