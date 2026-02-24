"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py5 Pre 0
    Team ID:        LC1 - 03
    Author:         Khai, wal64@purdue.edu
    Date:           2/22/2026 

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

def open_image(myImage):
    image = Image.open(myImage)
    
    is_grayscale = image.mode == "L"   # L = grayscale
    
    image = image.convert("RGB")
    image_array = np.array(image)
    
    return image_array, is_grayscale

def normalize_image(image):
    normal_image = image/255
    return normal_image

def linearize_image(image):
    linear = np.where(
        image <= 0.04045,
        image / 12.92,
        ((image + 0.055) / 1.055) ** 2.4
    )
    return linear

def mean_channel(img_array, n):
    if img_array.ndim == 2:
        return int(np.average(img_array))
    else:
        return int(np.average(img_array[:, :, n]))
def mean_channel_flt(img_array, n):
    if img_array.ndim == 2:
        return float(np.average(img_array))
    else:
        return float(np.average(img_array[:, :, n]))
        


def main():
    # print("Enter the filename of the image: grayscale_image.jpeg")
    currentImage = input("Enter the filename of the image: ")
    # currentImage = "color_image.jpeg"
    print(f"Image: {currentImage}")
    thisImage, is_grayscale = open_image(currentImage)
    normalized_image = normalize_image(thisImage)
    linearized_Image = linearize_image(normalized_image)

    if is_grayscale:
        red = green = blue = 0.00
    else:
        red = round(mean_channel_flt(linearized_Image, 0), 2)
        green = round(mean_channel_flt(linearized_Image, 1), 2)
        blue = round(mean_channel_flt(linearized_Image, 2), 2)
    print(f"Red Channel Mean: {red:.2f}")
    print(f"Green Channel Mean: {green:.2f}")
    print(f"Blue Channel Mean: {blue:.2f}")






if __name__ == "__main__":
    main()
