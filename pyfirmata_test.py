import pyfirmata
import time
import math

circle = .1 #number of seconds to turn 360 degrees
speed = .01
#board = pyfirmata.Arduino('/dev/tty96B0')
right_wheel = board.get_pin('d:9:o')
left_wheel = board.get_pien('d:10:o')

def draw(polar_points):
    print([point[1]/(2 * math.pi) * circle for point in polar_points])
    print([point[0] * speed for point in polar_points])
    for point in polar_points:
        print(point[1]/(2*math.pi)*circle)
        turn(right_wheel, point[1])
        time.sleep(1)
        straight(point[0])
        time.sleep(1)

def turn(pin, angle):
    pin.write(1)
    sleep_angle = angle/(2 * math.pi) * circle
    time.sleep(sleep_angle)
    pin.write(0)

def turn(direction):
    if direction == 'Right':
        turn(left_wheel, math.pi/2)
    elif direction == 'Left':
        turn(right_wheel, math.pi/2)

def straight(distance):
    right_wheel.write(1)
    left_wheel.write(1)
    time.sleep(distance * speed)
    right_wheel.write(0)
    left_wheel.write(0)
