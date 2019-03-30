import movement
import cv2

img = cv2.imread('heart.jpg',0)
movement.image_to_direction(img)
