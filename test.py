import movement
import cv2
import pyfirmata_test.py

img = cv2.imread('images/square.jpg',0)
points = movement.image_to_direction(img)

pyfirmata_test.move_rock(points)
