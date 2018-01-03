from Thermostat import Thermostat
from Thermometer import Thermometer
from Timer import Timer
import RPi.GPIO as GPIO
import time
from Triggerable import Triggerable
from threading import Thread

TOP_TIMER_PIN = 29
BOTTOM_TIMER_PIN = 28
TOP_RADIANT_PIN = 27
BOTTOM_RADIANT_PIN = 4
TOP_THERMOMETER_PIN = 5

if __name__ == "__main__":
    topTimerTrigger = Triggerable(TOP_TIMER_PIN)
    bottomTimerTrigger = Triggerable(BOTTOM_TIMER_PIN)
    topRadiantTrigger = Triggerable(TOP_RADIANT_PIN)
    bottomRadiantTrigger = Triggerable(BOTTOM_RADIANT_PIN)
    
    try:
        while True:
            topTimerTrigger.on()
            time.sleep(3)
            topTimerTrigger.off()
            time.sleep(3)
    except KeyboardInterrupt:
        print 'you killed me! :('
    finally:
        GPIO.cleanup()
    
    #topRadiantThermometer = Thermometer(TOP_THERMOMETER_PIN)
    #bottomRadiantThermometer = Thermometer(BOTTOM_THERMOMETER_PIN)

    #topRadiantThermostat = Thermostat(topRadiantTrigger, topRadiantThermometer)
    #bottomRadiantThermostat = Thermostat(bottomRadiantTrigger, bottomRadiantThermometer)
    #t1 = Thread(target=topRadiantThermostat.run)
    #t2 = Thread(target=bottomRadiantThermostat.run)
    #t1.start()
    #t2.start()