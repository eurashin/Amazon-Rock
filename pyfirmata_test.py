import pyfirmata

board = pyfirmata.Arduino('/dev/tty96B0')

board.digital[5].write(0)
