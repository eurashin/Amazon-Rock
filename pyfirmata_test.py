import pyfirmata
import math

circle = 2 #number of seconds to turn 360 degrees
right_wheel = 5
left_wheel = 6
speed = 1

def move_rock(polar_points):
    board = pyfirmata.Arduino('/dev/tty96B0')

    for point in polar_points: 
        turn(right_wheel, point[0])
        time.sleep(1)
        straight(point[1])
        time.sleep(1)
    


def turn(pin, angle): 
    board.digital[pin].write(1)
    time.sleep(angle/(2*math.pi) * circle)
    board.digital[pin].write(0)

def straight(distance): 
    board.digital[right_wheel].write(1)
    board.digital[left_wheel].write(1)
    time.sleep(distance * speed)
    board.digital[right_wheel].write(0)
    board.digital[left_wheel].write(0)
