
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT

class Thermometer:
    def __init__(self, pin_num, units='F', sensor=DHT.DHT22):
        self.pin_num = pin_num
        self.units = 'F'
        self.sensor = sensor
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup( pin_num, GPIO.IN )
    
    def get_reading(self):
        try:
            humidity, temperature_C = DHT.read_retry( self.sensor, self.pin_num )
            temperature_F = temperature_C * 9/5.0 + 32
        except KeyboardInterrupt:
            print 'You killed me :( '
        return temperature_F
    
    def get_reading_clean(self):
        return get_reading() + " " + self.units