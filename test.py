import movement
import cv2

img = cv2.imread('horse_outline.jpg',0)
movement.image_to_direction(img)
