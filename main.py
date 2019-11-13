###############################################################################
## Author: Team Supply Bot
## Edition: eYRC 2019-20
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv

########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))

## utility function
def adjust_angle(theta, x):
    if x < 0:
        theta += 180
    return theta


############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    rows,cols, _ = ip_image.shape

    pixel=[]
  #  for i in range(rows):
   #     for j in range(cols):
    for i in range(rows):
        for j in range(cols):
            pixel = ip_image[i, j]
            if list(pixel) == [0,0,255]:
                r_red = i
                c_red = j
            elif list(pixel) == [0, 255, 0]:
                r_green = i
                c_green = j
    r_red-=17
    c_red-=3
    r_green-=17
    c_red-=3
    xc, yc = int(rows/2), int(cols/2)
    xr, yr = c_red - xc, -r_red + yc
    xg, yg = c_green - xc, -r_green + yc

    theta1 = np.arctan(yr / xr)*180/np.pi
    theta2 = np.arctan(yg / xg)*180/np.pi

    theta2 = adjust_angle(theta2, xg)
    theta1 = adjust_angle(theta1, xr)
    theta = abs(theta2 - theta1)
    if  theta>180:
        theta=360-theta


    angle = round(theta,2)

    ## Your Code goes here
    ###########################
    #cv2.imshow("window", ip_image)
    #cv2.waitKey(0);
    return angle


####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    line = []
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path + "/" + image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        A = process(ip_image)
        ## saving the output in  a list variable
        line.append([str(i), image_name, str(A)])
        ## incrementing counter variable
        i += 1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path + "/" + 'angles.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(line)
    ## closing csv file    
    writeFile.close()


############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
