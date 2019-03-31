import pyfirmata
import time

board = pyfirmata.Arduino('/dev/tty96B0')
left_wheel = board.get_pin('d:9:o')
right_wheel = board.get_pin('d:10:o')

left_wheel.write(1)
time.sleep(2)
left_wheel.write(0)
time.sleep(1)
right_wheel.write(1)
time.sleep(2)
right_wheel.write(0)
