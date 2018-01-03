
import RPi.GPIO as GPIO
import time
import datetime from datetime

class Timer:
    """Timer class for reoccurring events, default to light cycle"""
    minutesPerHour = 60
    hoursPerDay = 24
    minutesPerDay = minutesPerHour * hoursPerDay
    photoperiod = 540

    def __init__(self, trigger, frequency=minutesPerDay, durationInMinutes=photoperiod):
        self.trigger = trigger
        self.frequency = frequency
        self.durationInMinutes = durationInMinutes
    
    def start(self):
        self.seedtime = datetime.datetime.now()
        while True:
            timeDif = datetime.now() - self.seedtime
            if timeDif.minutes >= self.duration:
                self.trigger.off()
                print 'Timer off\n'
            else:
                self.trigger.on()
                print 'Timer on\n'
            time.sleep(5)

