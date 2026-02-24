"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Use Matplotlib, pathlib, and Numpy to visualize color distribution in images (a histrogram of colors)

Assignment Information:
    Assignment:     Py5 Ind 0
    Team ID:        LC1 - 03
    Author:         Khai, wal64@purdue.edu
    Date:           2/24/2026 

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
from PIL import Image
from PIL import ImageOps
from pathlib import Path
import os

def open_image():
    these_images = []
    path = Path("Py5/images")
    files = list(path.iterdir())
    count = 0
    for images in files:

        print(f"{count +1}. {os.path.basename(images)}")
        opened_image = Image.open(images)
        img_array = np.array(opened_image)
        these_images.append(img_array)
        count +=1
    return these_images
       
def main():
    my_images = open_image()
    selcted_Image = input("Select an image (q to quit): ")





if __name__ == "__main__":
    main()
