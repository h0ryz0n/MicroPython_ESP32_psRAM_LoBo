import machine
import touchscreen as ts
import time

i2c = machine.I2C(scl=32, sda=23, speed=400000)

ts.init(i2c)
while True:
    ts.read()
    time.sleep(0.2)
