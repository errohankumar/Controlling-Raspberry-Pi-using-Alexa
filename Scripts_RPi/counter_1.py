import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

#for 1

GPIO.output(15,GPIO.HIGH)
GPIO.output(20,GPIO.HIGH)
GPIO.output(23,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(21,GPIO.LOW)
GPIO.output(18,GPIO.LOW)

print("number 1 on")
