import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import turtle


def max_length_index(arr):
    lengths = [len(arr_el) for arr_el in arr]
    return(lengths.index(max(lengths)))

#takes opencv image and gives set of arduino vector
def image_to_direction(open_img):
    #blank image (for testing)
    blank_image = np.zeros((500,500,3), np.uint8)

    #load the image
    ret, thresh = cv2.threshold(open_img, 127, 255, cv2.THRESH_BINARY) #apply threshold
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #find contours
    index = max_length_index(contours)

    #find approximization of our image
    cnt = contours[index]
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    points = [(approx[i, 0, 0], approx[i,0,1]) for i in range(len(approx))]
    points.append((approx[0, 0, 0], approx[0,0,1])) #close the loop!

    total_phi = 0
    polar_points = []
    for i in range(len(points) - 1): 
        move = direction(points[i], points[i+1], total_phi)
        total_phi = total_phi + move[1]
        polar_points.append(move)
    turtle_draw(polar_points)
    return(polar_points)




def direction(point1, point2, previous_phi):
    #point 1 is the 0,0
    point_prime = (point2[0] - point1[0], point2[1] - point1[1])
    rho = np.sqrt(point_prime[0]**2 + point_prime[1]**2)
    phi = 0
    if(point_prime[0] == 0): #straight up or down
        if(point_prime[1] > 0): #straight up
            phi = math.pi/2
        else: 
            phi = math.pi * 3/2
    elif(point_prime[1] == 0): #straight left or right
        if(point_prime[0] > 1): #stright right
            phi = 0
        else: 
            phi = math.pi
    else: 
        phi = np.arctan2(point_prime[1], point_prime[0])

    phi = phi - previous_phi
    return((rho, phi))
    

def show_image(img):
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def turtle_draw(polar_points): 
    turt = turtle.Turtle()
    for point in polar_points: 
        turt.left(math.degrees(point[1]))
        turt.forward(point[0])
    turt.done() 
