"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Find Waldo by using code to loop over an image and find simlarities

Assignment Information:
    Assignment:     py5 ind 2 
    Team ID:        LC1 - 03
    Author:         Khai, Wall64@purdue.edu
    Date:           02/28/2026

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


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def load_img(myImage):
    image = Image.open(myImage)

    # Check if grayscale
    if image.mode == "L":
        # Already grayscale
        image_array = np.array(image, dtype=np.float64) / 255.0
    else:
        # Convert color images to RGB
        image = image.convert("RGB")
        image_array = np.array(image, dtype=np.float64) / 255.0

    linear = np.where( ##linearize image
        image_array <= 0.04045,
        image_array / 12.92,
        ((image_array + 0.055) / 1.055) ** 2.4
    )


    return linear


def rgb_to_grayscale(rgb_img):#convert to grayscale

    R = rgb_img[:, :, 0]
    G = rgb_img[:, :, 1]
    B = rgb_img[:, :, 2]

    gray_img = 0.2126 * R + 0.7152 * G + 0.0722 * B

    return gray_img



import numpy as np

def ssd(I, T):
    I = np.array(I, dtype=np.float64)  # keep in 0-255 range
    T = np.array(T, dtype=np.float64)
    
    H, W = I.shape
    h, w = T.shape
    
    R_h = H - h + 1
    R_w = W - w + 1
    
    R = np.zeros((R_h, R_w), dtype=np.float64)
    
    for i in range(R_h):
        for j in range(R_w):
            patch = I[i:i+h, j:j+w]
            diff = patch - T
            R[i, j] = np.sum(diff**2)
    
    return R

def ssd_1(scene, template):
  
    # Convert to float64 to prevent overflow
    scene = scene.astype(np.float64)
    template = template.astype(np.float64)

    H, W = scene.shape
    h, w = template.shape

    # Precompute template squared sum
    template_sq_sum = np.sum(template**2)

    # Allocate result
    result = np.zeros((H - h + 1, W - w + 1), dtype=np.float64)

    # Compute SSD using nested loops (safe and simple)
    for i in range(H - h + 1):
        for j in range(W - w + 1):
            patch = scene[i:i+h, j:j+w]
            patch_sq_sum = np.sum(patch**2)
            cross_term = np.sum(patch * template)
            result[i, j] = patch_sq_sum - 2 * cross_term + template_sq_sum

    return result

def draw_rectangle(scene, template, map):#overlays a rectangle over the original image at the position of Waldo
    h, w = template.shape[:2]
    min_index = np.unravel_index(np.argmin(map), map.shape)
    y = int(min_index[0])
    x = int(min_index[1])
    print(f"The template is located at ({x}, {y}) ")#why is there an extra space here?

    plt.imshow(scene)
    plt.gca().add_patch(Rectangle((x,y), width=w, height=h, edgecolor='red', facecolor='none', lw=2))
    plt.show()
    return (x,y)#never asked us to return x, y but the autograder wanted this


def main():
    scenePath = input("Enter the path of the scene image you want to load: ")
    templatePath = input("Enter the path of the template image you want to load: ")

    # Load as uint8 grayscale for SSD
    scene_gray = np.array(Image.open(scenePath).convert("L"), dtype=np.uint8)
    template_gray = np.array(Image.open(templatePath).convert("L"), dtype=np.uint8)

    mappy = ssd_1(scene_gray, template_gray)

    # Load the scene as float for displaying
    loadedScene = load_img(scenePath)
    loadedTemplate = load_img(templatePath)
    draw_rectangle(loadedScene, loadedTemplate, mappy)#draw rectangle
    print("")#random line becuse they wanted one of these in the autograder for no reason

    
if __name__ == "__main__":
    main()#runs main lol
