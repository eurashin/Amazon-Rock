import pyfirmata
import time
import math

circle = .1 #number of seconds to turn 360 degrees
right_wheel = 9
left_wheel = 10
speed = .01
#board = pyfirmata.Arduino('/dev/tty96B0')

def move_rock(polar_points):
    print([point[1]/(2 * math.pi) * circle for point in polar_points])
    print([point[0] * speed for point in polar_points])
    for point in polar_points:
        print(point[1]/(2*math.pi)*circle)
        turn(right_wheel, point[1])
        time.sleep(1)
        straight(point[0])
        time.sleep(1)
    


def turn(pin, angle): 
    board.digital[pin].write(1)
    sleep_angle = angle/(2 * math.pi) * circle
    time.sleep(sleep_angle)
    board.digital[pin].write(0)

def straight(distance): 
    board.digital[right_wheel].write(1)
    board.digital[left_wheel].write(1)
    time.sleep(distance * speed)
    board.digital[right_wheel].write(0)
    board.digital[left_wheel].write(0)
