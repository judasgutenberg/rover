import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18,GPIO.OUT)
#GPIO.output(18, GPIO.HIGH)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
GPIO.output(21, GPIO.LOW)
pwm = GPIO.PWM(18, 1000)
pwm.start(5)
time.sleep(2)
pwm.stop()


#p = GPIO.PWM(23, 50)
#p.start(0)
#time.sleep(0)
#p.stop()
#GPIO.output(23, GPIO.LOW)

GPIO.cleanup()