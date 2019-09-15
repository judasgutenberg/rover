
import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

GPIO.setup(18,GPIO.INPUT)
GPIO.setup(20,GPIO.INPUT)
GPIO.cleanup()
 
