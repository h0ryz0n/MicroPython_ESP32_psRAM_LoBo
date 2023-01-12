import utime
import time
import pcf8563
from machine import I2C
from machine import Pin


def handle_interrupt(pin):
    if r.check_for_alarm_interrupt():
        print('is alarm clock interrupt')
    else:
        print('is not for alarm interrupt')
    r.clear_alarm()


irq = Pin(37, mode=Pin.IN, handler=handle_interrupt, trigger=Pin.IRQ_FALLING)
i2c = I2C(scl=22, sda=21)
r = pcf8563.PCF8563(i2c)

print('rtc time')
r.datetime()
time.sleep(1)

print('Clear alarm config register')
r.clear_alarm()

print('Setting current clock datetime')
r.write_all(50, 30, 15, 3, 17, 9, 49)

print('Set the alarm to match for minutes')
r.set_daily_alarm(minutes=31)

print('Enable rtc chip interrupt')
r.enable_alarm_interrupt()

while True:
    r.datetime()
    time.sleep(1)
