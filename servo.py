import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
pwm=GPIO.PWM(18,50)
pwm.start(0)


try:
    while 1:
        pwm.ChangeDutyCycle(2)
        time.sleep(1)
        pwm.ChangeDutyCycle(8)
        time.sleep(1)
        pwm.ChangeDutyCycle(16)
        time.sleep(1)
        
except:
    pwm.stop()
    GPIO.cleanup()
