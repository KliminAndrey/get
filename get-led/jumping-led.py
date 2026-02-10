import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

light_time = 0.2

period = 1.0

leds += reversed(leds)

for led in leds:
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)
