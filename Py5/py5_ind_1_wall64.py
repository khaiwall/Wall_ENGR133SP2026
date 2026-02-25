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

def display():
    count = 0
    strings = ["spongebob.jpg", "grayscale_landscape.jpeg", "landscape.jpeg"]   
    for string in strings:
        print(f"{count+1}. {string}")
        count +=1
    return strings
def load_image(images):

    opened_image = Image.open("Py5/images/" + images).convert("RGB")

    img_array = np.array(opened_image)
    if img_array.dtype == np.uint8:
        norm_img_array = img_array/255
        
        return norm_img_array            
    else:
        print("Image is not 8-bit.")

def linearize_image(image):
    linear = np.where(
        image <= 0.04045,
        image / 12.92,
        ((image + 0.055) / 1.055) ** 2.4
    )
    return linear


def calculate_luminance(image):
    R = np.average(image[:,:,0])
    G = np.average(image[:,:,1])
    B = np.average(image[:,:,2])
    Y = 0.2126*R + 0.7152*G + 0.0722*B
    print(f"The average luminance of the image: {Y:.3`f}")

def main():
    go = True
    while go:
        
        strings = display()
        selcted_Image = input("Select an image (q to quit): ")
        if selcted_Image == "q":
            go = False
        else:
            try:
                thisImage = int(selcted_Image)-1
                new_image = load_image(strings[thisImage])
                lin_image = linearize_image(new_image)
                luminance = calculate_luminance(lin_image)
                
            except ValueError:
                print("Invalid choice please try again.\n")



if __name__ == "__main__":
    main()