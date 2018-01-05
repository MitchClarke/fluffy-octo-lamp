
import Triggerable
import Thermometer
import time

heat = "HEAT"
cool = "COOL"

class Thermostat:

	def __init__(self, thermometer, triggerable, target=90, action=heat):
		self.target = target
		self.range = 1
		self.action = action
		self.thermometer = thermometer
		self.triggerable = triggerable
	
	def run(self):
		try:
			if (self.thermometer.get_temp() < self.target and self.action == heat) or\
				(self.thermometer.get_temp() > self.target and self.action == cool):
				self.triggerable.on()
				print 'relay on'
			else:
				self.triggerable.off()
				print 'relay off'
			time.sleep(5)
		except KeyboardInterrupt:
			print 'Thermostat keyboard interrupt'
			
	def adjust_temp(self, new_temp):
		self.target = new_temp

