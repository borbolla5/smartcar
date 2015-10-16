#!/usr/bin/env python2.7
import time
import RPi.GPIO as GPIO
import time
from pwm import PWM
from pid import PID
class Interrupt(object):
	"""Clase elaborada por Luis Borbolla para interrupcion por hardware en raspberry pi """
	def __init__(self, pin , pin_pwm , pin_pwmR):
		self.avance = 0 
		self.pin = pin
		self.pin_pwmR = pin_pwmR
		self.cuenta = 0
		self.index = 0 
		self.velocidad = 0
		self.tiempo_anterior = time.time()
		self.tiempo_actual = 0
		self.pin_pwm = pin_pwm
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self.interrupcion, bouncetime=5)
		GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self.pwm_llanta = PWM(self.pin_pwm)
		self.pwm_llantar = PWM(self.pin_pwmR)
		self.pid_vel  = PID()


	def setup(self , setPoint):
		self.pwm_llanta.start()
		if setPoint >0:
		    self.pwm_llanta.set_duty(setPoint/15.0)

		else:
		    self.pwm_llantar.set_duty(setPoint/15.0)
		self.pid_vel.setPoint(setPoint)
		
	def interrupcion(self,channel):
		#print 'velocidad = %s' % self.pin
		self.cuenta += 1
		self.tiempo_actual = time.time()
		self.avance += 10		
		prom_tiempos = (self.tiempo_actual-self.tiempo_anterior)/2
		self.velocidad = 9.974556675147593/prom_tiempos   #2.5*25.4*m.pi/20 == 9.974556675147593
	    	self.tiempo_anterior = self.tiempo_actual
		error = self.pid_vel.update(self.velocidad)
  		self.pwm_llanta.update(error/15.0)


	

	def esperar_int(self):
    	
		try:
    		    print "Waiting for rising edge on port 24"
    		    GPIO.wait_for_edge(24, GPIO.RISING)
    		    print "Rising edge detected on port 24. Here endeth the third lesson."

		except KeyboardInterrupt:
    		    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
		GPIO.cleanup()           # clean up GPIO on normal exit


if __name__ == '__main__':
	inte  = Interrupt(18,11,26)
	inte2 = Interrupt(22,21,23)
	#inte2.setup(500)	
	#inte.setup(34.55)
	i = 0
	while True:
		print i 

		time.sleep(1)
		#print 'cuenta = %s velocidad = %s' %( inte.cuenta,inte.velocidad)
		inte.cuenta = 0
		i +=1
