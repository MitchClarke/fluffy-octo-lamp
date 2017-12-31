
import RPi.GPIO as GPIO
import time
import Adafruit_DHT as DHT

RELAY_PIN = 21
DHT_PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup( RELAY_PIN, GPIO.OUT )
GPIO.setup( DHT_PIN, GPIO.IN )

sensor = DHT.DHT22
setTemp = 85
setHumidity = 60

try:
	while True:
		humidity, temperature_C = DHT.read_retry( sensor, DHT_PIN )
		temperature_F = temperature_C * 9/5.0 + 32
		
		print temperature_F, humidity
		
		if temperature_F < setTemp: 
			GPIO.output( RELAY_PIN, GPIO.LOW )
			print 'relay on'
		else:
			GPIO.output( RELAY_PIN, GPIO.HIGH )
			print 'relay off'
		time.sleep(5)
except KeyboardInterrupt:
	print 'You killed me :( '
finally:
	print 'cleaning up'
	GPIO.cleanup()
