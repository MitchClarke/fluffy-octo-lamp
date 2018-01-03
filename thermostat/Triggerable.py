
import RPi.GPIO as GPIO

class Triggerable:
    def __init__(self, pin_num):
        self.pin_num = pin_num
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( self.pin_num, GPIO.OUT )

    def on(self):
        print 'turning ' + str(self.pin_num) + ' high'
        GPIO.output( self.pin_num, GPIO.HIGH )

    def off(self):
        print 'turning ' + str(self.pin_num) + ' low'
        GPIO.output( self.pin_num, GPIO.LOW )
