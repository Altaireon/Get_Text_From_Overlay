# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np
import matplotlib.pyplot as plt

def getTextOverlay(input_image):
    threshold = 30
    print(input_image.shape)
    input_image = np.max(input_image,axis=2)
    print(input_image.shape)
    input_image[input_image<threshold] = 0
    input_image[input_image>threshold] = 255
    kernel_erode = np.ones((5,5),np.uint8)
    kernel_dilate = np.ones((5,5),np.uint8)
    input_image = cv2.dilate(input_image,kernel_dilate,iterations = 1) # to remove thin black lines
    input_image = cv2.erode(input_image,kernel_erode,iterations = 1) # to bring erooded text back to its original shape and size
    return input_image
    
    # Write your code here for output
    
    return output

if __name__ == '__main__':
    image = cv2.imread('data/simpsons_frame0.png')
#    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    output = getTextOverlay(image)
    plt.imshow(output)
    cv2.imwrite('simpsons_text.png',output)
#####################

