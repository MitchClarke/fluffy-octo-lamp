from Thermostat import Thermostat
from Thermometer import Thermometer
from Timer import Timer
import RPi.GPIO as GPIO
import time
from Triggerable import Triggerable
from threading import Thread

TOP_TIMER_PIN = 23
BOTTOM_TIMER_PIN = 12
TOP_RADIANT_PIN = 16
BOTTOM_RADIANT_PIN = 20
TOP_THERMOMETER_PIN = 21
#24,25,8
Triggerable(24).off()
Triggerable(25).off()
Triggerable(8).off()

if __name__ == "__main__":
    topTimerTrigger = Triggerable(TOP_TIMER_PIN)
    bottomTimerTrigger = Triggerable(BOTTOM_TIMER_PIN)
    bottomTimerTrigger.off()
    topRadiantTrigger = Triggerable(TOP_RADIANT_PIN)
    topRadiantTrigger.off()
    bottomRadiantTrigger = Triggerable(BOTTOM_RADIANT_PIN)
    bottomRadiantTrigger.off()
    try:
        while True:
            topTimerTrigger.on()
            time.sleep(3)
            topTimerTrigger.off()
            time.sleep(3)
			print str(GPIO.input(16)) + str(GPIO.input(20))
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