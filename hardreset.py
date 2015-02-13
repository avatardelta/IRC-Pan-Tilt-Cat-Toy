import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_14", GPIO.OUT)

def hard_reset():
	GPIO.output("P8_14", GPIO.HIGH)
#	GPIO.output("P8_14", GPIO.LOW)
	GPIO.cleanup()

if __name__ == "__main__":
	hard_reset()



