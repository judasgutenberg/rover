
import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)
GPIO.output(24, GPIO.LOW)

GPIO.setup(13,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.output(13, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
