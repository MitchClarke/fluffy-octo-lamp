import Thermostat
import Thermometer
import Timer
import time
from threading import Thread

TOP_TIMER_PIN = 1
BOTTOM_TIMER_PIN = 2
TOP_RADIANT_PIN = 3
BOTTOM_RADIANT_PIN = 4
TOP_THERMOMETER_PIN = 5

if __name__ == "__main__":
    topTimerTrigger = triggerable(TOP_TIMER_PIN)
    bottomTimerTrigger = triggerable(BOTTOM_TIMER_PIN)
    topRadiantTrigger = triggerable(TOP_RADIANT_PIN)
    bottomRadiantTrigger = triggerable(BOTTOM_RADIANT_PIN)
    
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