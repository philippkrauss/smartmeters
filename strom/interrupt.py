#! /usr/bin/python
import RPi.GPIO as GPIO
import time

INPUT_PIN = 21
COUNTER_FILE = "/home/pi/counter.txt"

counter = 0

try:
    file = open(COUNTER_FILE, "r")
    counter = int(file.read())
    file.close()
except Exception as e:
    print e


def my_callback(channel):
    global counter
    counter += 1
    file = open(COUNTER_FILE, "w")
    file.write(str(counter))
    file.close()
    print counter


GPIO.setmode(GPIO.BCM) 
GPIO.setup(INPUT_PIN, GPIO.IN) 

GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, my_callback, 100)

try:
  while True:
    time.sleep(0.5)

except KeyboardInterrupt:
  GPIO.cleanup()
