import movement
import time
import cv2
import pyfirmata_test

img = cv2.imread('images/square.jpg',0)
points = movement.image_to_direction(img)
print(points)
#time.sleep(15)
pyfirmata_test.move_rock(points)
