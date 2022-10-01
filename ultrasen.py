import Adafruit_BBIO.GPIO as GPIO
from time import sleep
import time
trig="P9_12"
echo="P9_11"
led="P9_13"
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
while(1):
        GPIO.output(trig,GPIO.LOW)
        print "sensor is settling pls wait ......."
        sleep(2)
        GPIO.output(led,GPIO.HIGH)
        sleep(0.05)
        GPIO.output(led,GPIO.LOW)
        sleep(0.05)
        GPIO.output(trig,GPIO.HIGH)
        sleep(0.00001)
        print "reading values"
        GPIO.output(trig,GPIO.LOW)
        while GPIO.input(echo)==0:
                start_time=time.time()
        while GPIO.input(echo)==1:
                bounceback_time=time.time()
        pulse_duration = bounceback_time - start_time
        distance = round(pulse_duration*17150,2)
        print distance
        if distance >=2000:
                print "range out_ move close objects .... \n "
                GPIO.output(led,GPIO.HIGH)
                sleep(5)
                GPIO.output(led,GPIO.LOW)
                sleep(5)
                print "starting  ......"
GPIO.cleanup()






