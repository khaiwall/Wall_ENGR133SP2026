
import math as m

#concerns sequences of integers in which each term is obtained from the previous term as follows: 
# If a term is even, the next term is one half of it. If a term is odd, the next term is 3 times the previous term plus 1.
#The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.
# - Wikipedia

def main():
    
    value = input("Type a number: ")

    intValue = int(value)

    while (intValue != 1):
        if (intValue%2 == 0):
            intValue = intValue/2

        else:
            intValue = (3*intValue) + 1
        print(round(intValue))

    # for i in range(1,2):
    #     myi = i
    #     while (i != 1):
    #         if (i%2 == 0):
    #             i = i/2

    #         else:
    #             i = (3*i) + 1
    #     print(round(myi), " converged")



if __name__ == "__main__":
    main()