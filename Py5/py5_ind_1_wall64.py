"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Use Matplotlib, pathlib, and Numpy to visualize color distribution in images (a histrogram of colors)

Assignment Information:
    Assignment:     Py5 Ind 1
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
import matplotlib.pyplot as plt
from pathlib import Path
import math as m
def display():
    count = 0
    strings = ["spongebob.jpg", "grayscale_landscape.jpeg", "landscape.jpeg"]   
    print("Available images:")
    for string in strings:
        print(f"{count+1}. {string}")
        count +=1
    return strings

def load_image(filename):
    image_path = filename

    opened_image = Image.open(image_path)    
    # opened_image = Image.open("Py5/images/" + image_path)    
    img_array = np.array(opened_image)

    if img_array.dtype != np.uint8:
        raise ValueError("Image is not 8-bit.")

    return img_array / 255
def linearize_image(image):
    linear = np.where(
        image <= 0.04045,
        image / 12.92,
        ((image + 0.055) / 1.055) ** 2.4
    )
    return linear


def calculate_luminance(image):
  
    if image.ndim==2:#Treate gray images differently
        Y = np.average(image)
    else: 
        R = np.average(image[:,:,0])
        G = np.average(image[:,:,1])
        B = np.average(image[:,:,2])
        Y = 0.2126*R + 0.7152*G + 0.0722*B
    
    print(f"The average luminance of the image: {Y:.3f}\n")
    return Y

    
def plot_pixel_intensity(image):

    if image.ndim==2:#treat gray images differently
            
        values = image.flatten()
        color = "Grayscale"

        fig, ax = plt.subplots() 
        ax.hist(values, bins=256, color='gray', alpha=0.5)
  
        ax.set_title(f"{color} Intensity Histogram")
        ax.set_xlabel("Pixel Value (0-255)")
        ax.set_ylabel("Quantity")
        plt.show()

    else:
            
        r_channel_values = 255*image[:, :, 0].flatten()
        g_channel_values = 255*image[:, :, 1].flatten()
        b_channel_values = 255*image[:, :, 2].flatten()
        color = "RGB"

        fig, ax = plt.subplots() 
        ax.hist(r_channel_values, bins=256, color='red', alpha=0.5)
        ax.hist(g_channel_values, bins=256, color='green', alpha=0.5)
        ax.hist(b_channel_values, bins=256, color='blue', alpha=0.5)
        ax.set_title(f"{color} Intensity Histogram")
        ax.set_xlabel("Pixel Value (0-255)")
        ax.set_ylabel("Quantity")
        plt.show()

def main():
    go = True
    while go:
        
        strings = display()
        selected_Image = input("Select an image (q to quit): ")
        # selected_Image = "1"
        if selected_Image == "q":
            go = False
        elif selected_Image.isdigit():
            
            thisImage = int(selected_Image)-1
            new_image = load_image("images/" + strings[thisImage])
            # new_image = load_image(strings[thisImage])
            new_image = load_image(strings[thisImage])
            lin_image = linearize_image(new_image)
            luminance = calculate_luminance(lin_image)
            plot_pixel_intensity(lin_image)
            
        else:
            print("Invalid choice, please try again.\n")



if __name__ == "__main__":
    main()