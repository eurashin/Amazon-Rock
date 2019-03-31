from GPIOLibrary import GPIOProcessor
import time


GP = GPIOProcessor()

try:
    Pin27 = GP.getPin27()
    Pin27.out()

    for i in range(0,20):
        Pin27.high()
        time.sleep(1)
        Pin27.low()
        time.sleep(1)

finally:
    GP.cleanup()
