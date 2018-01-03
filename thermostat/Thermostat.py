
import triggerable
import RPi.GPIO as GPIO
import time

class Thermostat:
	heat = "HEAT"
	cool = "COOL"
	
	def __init__(self, thermometer, triggerable, target=90, range=1, action=heat):
		self.target = target
		self.range = 1
		self.action = action
		self.thermometer = thermometer
		self.triggerable = triggerable
	
	def run(self):
		try:
			while True:
				if (thermometer.get_temp() < self.target and self.action == heat) or\
					(thermometer.get_temp() > self.target and self.action == cool): 
					self.triggerable.on()
					print 'relay on'
				else:
					self.triggerable.off()
					print 'relay off'
				time.sleep(5)
		except KeyboardInterrupt:
			print 'You killed me :( '
			
	def adjust_temp(self, new_temp):
		self.target = new_temp
