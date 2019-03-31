import movement
import cv2

img = cv2.imread('images/octocat.jpg',0)
print(movement.image_to_direction(img))

