import time
class Led:
    def __init__(self, pin):
        self.pin = pin
    
    def light(self):
        print("Lighting on pin: {}".format(self.pin))
    
    def light_n_times(self, times):
        for n in range(times):
            self.light()
    
led = Led(2)
led.light()
led.light_n_times(4)

def foo(tim=1):
    print("Hello")
    time.sleep(tim)
    print("Hello")

foo()