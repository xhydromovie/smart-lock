import RPi.GPIO as GPIO
import time

class Button:
    def __init__(self, pin):
        self.buttonPin = pin
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def state(self):
        return GPIO.input(self.buttonPin)

def foo():
  print("Start")
  time.sleep(3)
  print("End - recognized")

def low():
  print("low")
  time.sleep(0.5)

ledPin = 12
buttonPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

button = Button(buttonPin)

while True:
  buttonState = button.state()
  if buttonState == False:
    GPIO.output(ledPin, GPIO.HIGH)
    foo()
  elif buttonState == True:
    low()

