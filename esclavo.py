#!/usr/bin/env python
from interrupcion import Interrupt
from pwm import PWM
from rgb import RGB
from mysql import Database
from pid import PID
from excel import Excel
from ssh import SSH
from lectura import Lectura
import RPi.GPIO as GPIO
import math as m 
import time
import sys

class Esclavo(object):
	"""Clase desarrollada por Luis Borbolla 
		para procesamiento de informacion en el raspberry pi , 
		siendo el maestro la clase principal ejecutada desde 
		una computadora remota"""
	def __init__(self):
		self.lectura_izq     = Interrupt(22,21,26)
		self.lectura_izq.pwm_llanta.start()
		self.lectura_izq.pid_vel.setPoint(150)
		self.lectura_der = Interrupt(18,23,11)
		self.lectura_der.pwm_llanta.start()
		self.lectura_der.pid_vel.setPoint(150)
		self.rgb             = RGB([3,5,7])
		self.escribir = Lectura('datos_pid.csv')
		'''AJUSTES SSH'''
		'''self.ssh = SSH()
		self.ssh.host = '192.168.15.100'
		self.username = 'bojack'
		self.ssh.conectar()'''
		#self.excel = Excel() 
		#self.mysql 	         = Database()
		#self.foco_izq		 = Led(13)
		#self.foco_der		 = Led(11)
		self.perimetro = m.pi * (2.54*2.5)
		
		i = 0
		'''AJUSTES PID IZQ'''
		self.lectura_izq.pid_vel.setKp(0.400)
		self.lectura_izq.pid_vel.setKi(0.020)
		self.lectura_izq.pid_vel.setKd(0.0)
		#self.lectura_izq.setup(300)

		'''AJUSTES PID DER'''
		self.lectura_der.pid_vel.setKp(0.400)
                self.lectura_der.pid_vel.setKi(0.020)
                self.lectura_der.pid_vel.setKd(0.0)
                #self.lectura_der.setup(300)	
if __name__ == '__main__':

	velocidad = float(sys.argv[1]) 
	carro = Esclavo()
	carro.lectura_izq.setup(velocidad)
	carro.lectura_der.setup(velocidad) 
	carro.escribir.abrir()
	#carro.ssh.borrar('Dropbox/lab_control/archivos_conf/pid_izq.txt')
	i = True
	inicio2 = time.time()
	inicio = int(round(time.time() * 1000))	
	while i:
		time.sleep(0.01)		
		try:
		    tiempo = (int(round(time.time() * 1000))-inicio)/60.
		    #pidizq = carro.ssh.leer_archivo('Dropbox/lab_control/archivos_conf/pid_izq.txt')
		    #carro.ssh.escribir('Dropbox/lab_control/archivos_conf/pid_izq.txt',pidizq,'%s %s %s %s \n'%(tiempo,0,tiempo,carro.lectura_izq.velocidad))		    
                    carro.escribir.escribir( '\n%s\t%s\t%s\t%s\t%s\tavance : %s\t\t\t%s\t%s\t%s\t%s\t%s\tavance : %s ' % (carro.lectura_izq.pin,
								carro.lectura_izq.velocidad , 
								carro.lectura_izq.pid_vel.set_point ,
								carro.lectura_izq.pid_vel.set_point-carro.lectura_izq.velocidad,
								carro.lectura_izq.pwm_llanta.dc,
								carro.lectura_izq.avance,
								carro.lectura_der.pin,
                                                                carro.lectura_der.velocidad ,
                                                                carro.lectura_der.pid_vel.set_point ,
                                                                carro.lectura_der.pid_vel.set_point-carro.lectura_der.velocidad,
                                                                carro.lectura_der.pwm_llanta.dc,
                                                                carro.lectura_der.avance))
		
		    t = time.time()
		    if t-inicio2>6:
			i = not i
			carro.escribir.cerrar()
                except KeyboardInterrupt:
                    GPIO.cleanup()
         

	'''
        diferencia = carro.lectura_der.avance-carro.lectura_izq.avance
	print diferencia
        if diferencia < 0:
            while diferencia != 0:
                carro.lectura_izq.setup(100)

        else:
            while diferencia !=0:
                carro.lectura_der.setup(100)'''

	#carro.ssh.desconectar()	
	GPIO.cleanup()
