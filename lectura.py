#!/usr/bin/env python

import random

class Lectura(object):
	"""docstring for Lectura"""
	def __init__(self,archivo):
		print 'objeto Lectura instanciado!'
		self.archivo = archivo
		self.velocidad = []
		self.angulo = []


		


	def read(self):
		archivo = open(self.archivo, 'r')
		for linea in archivo:
			print linea
			matriz = linea.split(',')
			self.velocidad.append(matriz[0])
			self.angulo.append(matriz[1])

		archivo.close()

		#print 'Velocidad \n %s \nAngulo \n %s \n' %(self.velocidad , self.angulo)

	def abrir(self):
		self.archivo =  open(self.archivo , 'w')
	def escribir(self,linea):
		
		self.archivo.write(linea)

	def cerrar(self):
		self.archivo.close()
	
	def borrar(self):
		archivo = open(self.archivo , 'w')
		archivo.close()
if __name__ == '__main__':
	cocks = Lectura('conf.txt')
	#cocks.escribir('i')
	
	cocks.read()
	print 'coke \n %s'% cocks.velocidad
