#!/usr/bin/rnv python 
import RPi.GPIO as GPIO
import time
import sys
class RGB(object):
	"""Clase escrita por luis Borbolla , para controlar un led RGB de Cathodo comun """
	def __init__(self, rgb):
		self.rgb   	  = rgb
		self.rojo 	  = [0,1,1]
		self.verde 	  = [1,0,1]
		self.azul  	  = [1,1,0]
		self.amarillo = [0,0,1]
		self.magenta  = [0,1,0]
		self.cian     = [1,0,0]
		self.blanco   = [0,0,0]
		GPIO.setmode(GPIO.BOARD)
		print 'RGB instanciado '
		for pin in rgb:
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin,True)

	def frojo(self):
		for i in range(3):
			GPIO.output(self.rgb[i],self.rojo[i])
		

	def fverde(self):
		for i in range(3):
			GPIO.output(self.rgb[i],self.verde[i])

	def fazul(self):
		for i in range(3):
			GPIO.output(self.rgb[i],self.azul[i]	)				

	def famarillo(self):
		for i in range(3):
			GPIO.output(self.rgb[i],self.amarillo[i])

	def fmagenta(self):
		for i in range(3):
			GPIO.output(self.rgb[i],self.magenta[i]	)			
	
	def fcian(self):
		for i in range(3):
			GPIO.output(self.rgb[i],self.cian[i]	)

	def fblanco(self):
		for i in range(3):
			GPIO.output(self.rgb[i],self.blanco[i])

	def fapagar(self):
		for i in range(3):
			GPIO.output(self.rgb[i],1)
				
if __name__ == '__main__':
	led = RGB([3,5,7])
	#arg = ['Nada','rojo','verde','azul','amarillo','violeta','cian','blanco','pruebas']
	accion = sys.argv[1]
	if accion == 'verde':
		led.fverde()
		time.sleep(1)
		led.fapagar()

	if accion == 'rojo':
		led.frojo()
		time.sleep(1)
		led.fapagar()	

	if accion == 'azul':
		led.fazul()
		time.sleep(1)
		led.fapagar()
	
	if accion == 'amarillo':
		led.famarillo()
		time.sleep(1)
		led.fapagar()	

	if accion == 'magenta':
		led.fmagenta()
		time.sleep(1)
		led.fapagar()

	if accion == 'cian':
		led.fcian()
		time.sleep(1)
		led.fapagar()		
	
	if accion == 'blanco':
		led.fblanco()
		time.sleep(1)
		led.fapagar()

	if accion =='pruebas':

		try:
			led.frojo()
			time.sleep(1)
			led.fverde()
			time.sleep(1)
			led.fazul()
			time.sleep(1)
			led.famarillo()
			time.sleep(1)
			led.fmagenta()
			time.sleep(1)
			led.fcian()
			time.sleep(1)
			led.fblanco()
			time.sleep(1)
			led.fapagar()
		except KeyboardInterrupt:
			GPIO.cleanup()
	

	if accion =='fverde':
		led.fverde()
	if accion == 'apagar':
		led.fapagar()	
	if accion == 'famarillo':
		led.famarillo()
	if accion == 'frojo':
                led.frojo()
