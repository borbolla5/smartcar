import time 
import RPi.GPIO as GPIO
import sys
class PWM(object):
    """docstring for PWM"""
    def __init__(self, pin):

        self.pin = pin
        self.dc = 0
	self.dc_antes = 0
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 500)  # channel=12 frequency=50Hz
        
    def start(self):
        self.pwm.start(0)

    def stop(self):
        self.pwm.stop()


    def set_duty(self,dc):    
	if dc < 0:
	    dc = -dc
        self.pwm.ChangeDutyCycle(dc)
	self.dc_antes = self.dc
        self.dc = dc

        
    def update(self , error):
        current = self.dc + error 
        if current > 100:
            current = 100
        elif current < 0:
            current = 0
	#print 'current = %s ' %current
        self.set_duty(current)



if __name__ == '__main__':
    izq = sys.argv[1]
    der = sys.argv[2]
    direccion = bool(int(sys.argv[3]))
    print izq
    print der
    if direccion:
        a = PWM(21)
        b = PWM(23)
        a.start()
        b.start()
        a.set_duty(int(izq))
        b.set_duty(int(der))
        time.sleep(3)   
        a.stop()
        b.stop()

    if not direccion:
        a = PWM(26)
        b = PWM(11)
        a.start()
        b.start()
        a.set_duty(int(izq))
        b.set_duty(int(der))
        time.sleep(3)   
        a.stop()
        b.stop()
