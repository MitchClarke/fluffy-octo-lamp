from Thermostat import Thermostat
from Thermometer import Thermometer
from Timer import Timer
import time
from Triggerable import Triggerable
from threading import Thread

TOP_TIMER_PIN = 40
BOTTOM_TIMER_PIN = 38
TOP_RADIANT_PIN = 36
BOTTOM_RADIANT_PIN = 32
TOP_THERMOMETER_PIN = 22

if __name__ == "__main__":
    topTimerTrigger = Triggerable(TOP_TIMER_PIN)
    bottomTimerTrigger = Triggerable(BOTTOM_TIMER_PIN)
    topRadiantTrigger = Triggerable(TOP_RADIANT_PIN)
    bottomRadiantTrigger = Triggerable(BOTTOM_RADIANT_PIN)
    
    while True:
        topTimerTrigger.on()
        time.sleep(3)
        topTimerTrigger.off()
        time.sleep(3)
    
    #topRadiantThermometer = Thermometer(TOP_THERMOMETER_PIN)
    #bottomRadiantThermometer = Thermometer(BOTTOM_THERMOMETER_PIN)

    #topRadiantThermostat = Thermostat(topRadiantTrigger, topRadiantThermometer)
    #bottomRadiantThermostat = Thermostat(bottomRadiantTrigger, bottomRadiantThermometer)
    #t1 = Thread(target=topRadiantThermostat.run)
    #t2 = Thread(target=bottomRadiantThermostat.run)
    #t1.start()
    #t2.start()