import movement
import cv2

img = cv2.imread('images/uk.png',0)
movement.image_to_direction(img)
