import RPi.GPIO as GPIO

class Button:
    def __init__(self, pin):
        self.buttonPin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def state(self):
        return GPIO.input(self.buttonPin)