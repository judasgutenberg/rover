import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setup(24,GPIO.OUT)
GPIO.output(24, GPIO.HIGH)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.output(19, GPIO.HIGH)
GPIO.output(26, GPIO.LOW)
for x in range(0,5):
	GPIO.output(24, GPIO.HIGH)
 	time.sleep(0.02)
	GPIO.output(24, GPIO.LOW)
	time.sleep(0.08)
GPIO.output(24, GPIO.LOW)
	
 
