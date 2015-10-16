# smartcar

-------------------------------------------------------------------------------------------------
+
+
+Autor : Luis Borbolla 
+Fecha : 16/Oct/15
+correo: luis@4suredesign.com
+
+
+------------------------------------------------------------------------------------------------
Codigo para controlador PID de carrito 

El codigo en este proyecto , sirve para controlar por medio de un PID de velocidad el carrito como se muestra en la imagen siguiente 

http://mlm-s1-p.mlstatic.com/kit-chasis-carro-robot-2wd-para-arduino-pic-se-el-mejor--860001-MLM20253708832_022015-F.jpg

pero puede funcionar con cualquier carrito , que utilize motor de corriente directa , y se realice un encoder para las interrupciones 

El codigo esta probado en Raspberry pi model B 

-conexion de los pines para interrupcion se puede encontrar en este tutorial 

http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio

-optointerruptor utilizado 

http://www.steren.com.mx/optointerruptor-integrado-de-30-volts-1-amper.html

USO :

al descargar el proyecto , ejecutar en la terminal , en la carpeta donde se encuentre el proyecto , 

python esclavo.py 800

donde el numero 800 sera la velocidad a la que se requiera que el carro avance , controlado por el PID de velocidad

para mayor informacion o dudas : luis@4suredesign.com
