#!/usr/bin/python
import serial
import sys
import signal
import array
import os
import chardet
from time import sleep

stop_flag = False
global time
time=0
def interrupt(a,b): #keyboard interrupt ctrl+c
	print"stop"
	global stop_flag
	stop_flag = True


def hexShow(argv):  #ascii to hex
    result = ''  
    hLen = len(argv)  
    for i in xrange(hLen):  
        hvol = ord(argv[i])  #ascii to int
        hhex = '%02x'%hvol  
        result += hhex+' '  
    print 'hexShow:',result 

signal.signal(signal.SIGINT, interrupt) #keyboard interrupt signal

try:
	ser = serial.Serial('/dev/ttyUSB0', 9600) #set serial port
	print ser.portstr

except Exception, e_msg:
	print 'open serial failed.'
	print e_msg
	exit(1)

print 'A Serial Echo Is Running...'

counter = 0
I_set = 0.3

n = ser.write('syst:rem\n')
n = ser.write('POW 0\n')
while True:
	sleep(0.1) #10Hz Loop
	time=time+0.1
	if time<=34:
		#n1=ser.write('POW 100\n')

		n1=ser.write('POW '+ str(30*time) +'\n')
		
		#sleep(0.005)
		n2=ser.write('FETC:VOLT?\n')
		
		#sleep(0.005)
		n3=ser.write('FETC:CURR?\n')

		data=''
		#sleep(0.005)
		n4=ser.write('FETC:POW?\n')

		while ser.inWaiting() > 0:
			p=ser.read(1)
			data += p
		if counter > 0:
			data=data.split('\n') 
			#print data
			vol = data[0]
			voltage = float(vol)
			print voltage



	elif time<=47:
		n1=ser.write('POW 1050')
		sleep(0.001)
		n2=ser.write('FETC:VOLT?\n')
		sleep(0.001)

		voltage=''
		while ser.inWaiting() > 0:
			v=ser.read(1)
			voltage += v
		print 'voltage='+voltage
		
		n3=ser.write('FETC:CURR?\n')
		sleep(0.001)
		current=''
		while ser.inWaiting() > 0:
			i=ser.read(1)
			current += i
		print 'current'+current
		
		n4=ser.write('FETC:POW?\n')
		sleep(0.001)
		power=''
		while ser.inWaiting() > 0:
			p=ser.read(1)
			power += p
		print 'power='+power 
		
	elif time<=50:
		n1=ser.write('POW 1050-150*(t-50)\n')
		sleep(0.001)
		n2=ser.write('FETC:VOLT?\n')
		sleep(0.001)

		voltage=''
		while ser.inWaiting() > 0:
			v=ser.read(1)
			voltage += v
		print 'voltage='+voltage
		
		n3=ser.write('FETC:CURR?\n')
		sleep(0.001)
		current=''
		while ser.inWaiting() > 0:
			i=ser.read(1)
			current += i
		print 'current'+current
		
		n4=ser.write('FETC:POW?\n')
		sleep(0.001)
		power=''
		while ser.inWaiting() > 0:
			p=ser.read(1)
			power += p
		print 'power='+power 
		
	else:
		break
	####### send #######
	
	#n = ser.write('STAT:QUES:EVEN?')
	#if counter == 50:
	#	n = ser.write('CURR 5 CURR:LEV '+I_set) ##is it right??????
	#	counter = 0

	####### read #######
	 #buffer: 1 bytes
	#s=s.decode("asci
	#hexShow(s)  

	#fencoding=chardet.detect(s)  #dectect data encode type
	#print fencoding

	counter = counter + 1
	if counter == 100:
		counter = 1
	
	if stop_flag:
		break

print 'Program interrupted!'







