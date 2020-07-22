#!/usr/bin/python

import RPi.GPIO as GPIO
import RPi.GPIO
import time
import cwiid

from threading import Thread

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER = 25
GPIO_ECHO = 7
pinLED_rojo1 = 20
pinLED_rojo2 = 21

pinLED_chulo_1 = 24
pinLED_chulo_2 = 23
pinLED_chulo_3 = 27


pinPWM_dcha = 16 #motor a manejar

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)
GPIO.setup(pinLED_rojo1, GPIO.OUT)
GPIO.setup(pinPWM_dcha, GPIO.OUT)
GPIO.setup(pinLED_rojo2, GPIO.OUT)

#LED chulo
GPIO.setup(pinLED_chulo_1, GPIO.OUT)
GPIO.setup(pinLED_chulo_2, GPIO.OUT)
GPIO.setup(pinLED_chulo_3, GPIO.OUT)



#GPIO.setmode(GPIO.BOARD)
#pins (2,3,4,17) wii_mote


pinPWM_dcha_reverse = 11 #10
pinPWM_izda = 12 #5
pinPWM_izda_reverse = 13 #11

pinLED_azul1 = 18 #4
pinLED_azul2 = 18 #4
pinLED_amarillo_izda = 29 #2
pinLED_amarillo_dcha = 31 #11

button_delay = 0.1

def Variador_colores_LED():
	mutex.acquire()
	contador = 0
	mutex.release()
	while(1):
		if(contador == 0):
			GPIO.output(pinLED_chulo_1, True)
			GPIO.output(pinLED_chulo_2, True)
			GPIO.output(pinLED_chulo_3, True)
			contador = (contador+1)%3
		elif(contador == 1):
			GPIO.output(pinLED_chulo_1, True)
			GPIO.output(pinLED_chulo_2, True)
			GPIO.output(pinLED_chulo_3, False)
			contador = (contador+1)%3
		else:
			GPIO.output(pinLED_chulo_1, True)
			GPIO.output(pinLED_chulo_2, False)
			GPIO.output(pinLED_chulo_3, False)
			contador = (contador+1)%3

def encender_led():
		GPIO.output(pinLED_rojo1, True)
		GPIO.output(pinLED_rojo2, True)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, False)
		GPIO.output(pinLED_rojo2, False)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, True)
		GPIO.output(pinLED_rojo2, True)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, False)
		GPIO.output(pinLED_rojo2, False)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, True)
		GPIO.output(pinLED_rojo2, True)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, False)
		GPIO.output(pinLED_rojo2, False)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, True)
		GPIO.output(pinLED_rojo2, True)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, False)
		GPIO.output(pinLED_rojo2, False)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, True)
		GPIO.output(pinLED_rojo2, True)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, False)
		GPIO.output(pinLED_rojo2, False)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, True)
		GPIO.output(pinLED_rojo2, True)
		time.sleep(1)
		GPIO.output(pinLED_rojo1, False)
		GPIO.output(pinLED_rojo2, False)
		time.sleep(1)

def Demas_Coche():
	conectado = False
	print 'Presiona 1 + 2 en el mando de wii ...'
	time.sleep(1)
	try:
		wii = cwiid.Wiimote()
		conectado = True
	except RuntimeError:
		print ("Error, no se puede acceder al mando de wii T_T")
		print ("Se ha calado el coche")
		conectado = False
		GPIO.cleanup
		quit()



	print ("Mando de la wii conectado :D...\n")
	print ("Por favor, presiona algunos botones para comprobar la conexion.\n")
	print ("Presiona + y - para desconectar el mando de la wii y finalizar.\n")


	wii.rpt_mode = cwiid.RPT_BTN

	while True:

		buttons = wii.state['buttons']
		#COmprobamos conexion con mando wii
			#Apagamos motor
		if(buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
			print ("\nApagando motores...")
			wii.rumble = 1
			time.sleep(1)
			wii.rumble = 0
			exit(wii)
			conectado = False

			#botones del mnado pulsados
		if (buttons & cwiid.BTN_LEFT):
			print 'Left pressed'

			time.sleep(button_delay)
			#io.output(2, True)

		if(buttons & cwiid.BTN_RIGHT):
			print 'Right pressed'
			#time.sl(button_delay)
			#io.output(3, True)

		if (buttons & cwiid.BTN_UP):
			print 'Up pressed'
			time.sleep(button_delay)
			#io.output(4, True)

		if (buttons & cwiid.BTN_DOWN):
			print 'Down pressed'
			time.sleep(button_delay)
			#io.output(17, True)

		if (buttons & cwiid.BTN_1):
			print 'Button 1 pressed'
			GPIO.output(pinLED_rojo1, True)
		#else:
			#GPIO.output(pinLED_rojo1, False)

		if (buttons & cwiid.BTN_2):
			print 'Button 2 pressed'
			GPIO.output(pinLED_rojo2, True)
		#else:
		#	GPIO.output(pinLED_rojo2, False)

			#Arrancamos el ventilador cuando pulsamos A
		if (buttons & cwiid.BTN_A):
				print 'Button A pressed'
				time.sleep(button_delay)

				GPIO.output(pinPWM_dcha, True)
		#else:
		#		GPIO.output(pinPWM_dcha, False)

		if (buttons & cwiid.BTN_B):
				print 'Button B pressed'
				time.sleep(button_delay)

		if (buttons & cwiid.BTN_HOME):
				print 'Home Button pressed'
				time.sleep(button_delay)

		if (buttons & cwiid.BTN_MINUS):
				print 'Minus Button pressed'
				time.sleep(button_delay)

		if (buttons & cwiid.BTN_PLUS):
				print 'Plus Button pressed'
				time.sleep(button_delay)


		#Manejo del cochezuco
		if(conectado == True):
			GPIO.output(GPIO_TRIGGER, True)
			time.sleep(0.05)
			GPIO.output(GPIO_TRIGGER, False)
			empezamos = time.time()

			#Manejamos los led con el mando a la vez q el sensor
			if (buttons & cwiid.BTN_LEFT):
				print 'Left pressed'
				time.sleep(button_delay)
				G

				#io.output(2, True)

			if(buttons & cwiid.BTN_RIGHT):
				print 'Right pressed'
				time.sleep(button_delay)
				#io.output(3, True)

			while  GPIO.input(GPIO_ECHO) == 0: #Sensor no recibe la seal
				empezamos = time.time()
				conectado = False
			while GPIO.input(GPIO_ECHO) == 1: #Sensor por fin recibe seal
				fin = time.time()

			tiempo_rebote_senial = fin - empezamos
			distancia = (tiempo_rebote_senial * 34300)/2
			print (distancia)
			print ("cm")
			time.sleep(1)

			if(distancia < 40):
				GPIO.output(pinLED_rojo1, True)
				GPIO.output(pinLED_rojo2, True)
			else:
				GPIO.output(pinLED_rojo1, False)
				GPIO.output(pinLED_rojo2, False)


		#Si se pierde conexin con el mando o se manda seal de parar, se apaga el coche
	 	if conectado == False:

			GPIO.cleanup

# main o loop como quieras llamarlo

#Ejecucion en paralelo del resto de funcionalidades
#print 'Inicio ejecucion resto coche'
thread1 = Thread(target = encender_led())
thread2 = Thread(target2 = Demas_Coche())

thread1.start()
thread2.start()
