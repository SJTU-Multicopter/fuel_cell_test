#!/usr/bin/python
import serial
import sys
import signal
import array
import os
import chardet
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation  
from time import sleep
from numpy import *
import math

global mode
mode = 1

stop_flag = False
global time
global m
global voltage
global current
global power
global power1


x=[i/10.0 for i in range(1200)]
vp=zeros(1200)
cp=zeros(1200)
pp=zeros(1200)
p1p=zeros(1200)

m=-1
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


fig = plt.figure() 
ax1 = fig.add_subplot(3,1,1,xlim=(0, 120), ylim=(0, 30)) #graph length, height, index, x range, y range
ax2 = fig.add_subplot(3,1,2,xlim=(0, 120), ylim=(0, 50))
ax3 = fig.add_subplot(3,1,3,xlim=(0, 120), ylim=(0,1100))
line1, = ax1.plot([], [], lw=2) 
line2, = ax2.plot([], [], lw=2) 
line3, = ax3.plot([], [], lw=2)  
line4, = ax3.plot([], [], lw=2)
def init():  
	line1.set_data([], [])  
	line2.set_data([], [])  
	line3.set_data([], [])
	line4.set_data([], [])

	return line1,line2,line3, line4

# animation function.  this is called sequentially   
def animate(i):

	global time
	global voltage
	global current
	global power
	global power1
	time=time+0.1
	voltage=0
	current=0
	power=0
	power1=0
		#n1=ser.write('POW 100\n')
	if time<=40:
		power1=25*time
		n1=ser.write('POW '+ str(power1) +'\n')
		n2=ser.write('FETC:VOLT?\n')
		n3=ser.write('FETC:CURR?\n')
		data=''
		n4=ser.write('FETC:POW?\n')
		while ser.inWaiting() > 0:
			p=ser.read(1)
			data += p
		if time > 0.1:
			data=data.split('\n') 
		#print data
			vol = data[0]
			voltage = float(vol)
			print voltage
			current = float(data[1])
			print current
			power = float(data[2])
			print power
			print power1

	elif time<=80:
		global mode
		if mode == 1:
			power1=1000
			n1=ser.write('POW '+str(power1)+'\n')
			n2=ser.write('FETC:VOLT?\n')
			n3=ser.write('FETC:CURR?\n')
			n4=ser.write('FETC:POW?\n')
			data=''
			while ser.inWaiting() > 0:
				p=ser.read(1)
				data += p
			if time > 0.1:
				data=data.split('\n') 
				#print data
				vol = data[0]
				voltage = float(vol)
				print voltage
				current = float(data[1])
				print current
				power = float(data[2])
				print power
				print power1

		elif mode == 2:
			#power1=500+500*math.sin(time)
			power1=500+500*math.sin((time - 40 + 1.57)*1)
			n1=ser.write('POW '+str(power1)+'\n')
			n2=ser.write('FETC:VOLT?\n')
			n3=ser.write('FETC:CURR?\n')
			n4=ser.write('FETC:POW?\n')
			data=''
			while ser.inWaiting() > 0:
				p=ser.read(1)
				data += p
			if time > 0.1:
				data=data.split('\n') 
				#print data
				vol = data[0]
				voltage = float(vol)
				print voltage
				current = float(data[1])
				print current
				power = float(data[2])
				print power
				print power1

		elif mode == 3:
			power1= 1000 + 200 * math.sin((time - 40)*1)
			n1=ser.write('POW '+str(power1)+'\n')
			n2=ser.write('FETC:VOLT?\n')
			n3=ser.write('FETC:CURR?\n')
			n4=ser.write('FETC:POW?\n')
			data=''
			while ser.inWaiting() > 0:
				p=ser.read(1)
				data += p
			if time > 0.1:
				data=data.split('\n') 
				#print data
				vol = data[0]
				voltage = float(vol)
				print voltage
				current = float(data[1])
				print current
				power = float(data[2])
				print power
				print power1

		elif mode == 4:
			if time < 50:
				power1 = 900
			elif time < 60:
				power1 = 1100
			elif time < 70:
				power1 = 900
			else:
				power1 = 1100

			n1=ser.write('POW '+str(power1)+'\n')
			n2=ser.write('FETC:VOLT?\n')
			n3=ser.write('FETC:CURR?\n')
			n4=ser.write('FETC:POW?\n')
			data=''
			while ser.inWaiting() > 0:
				p=ser.read(1)
				data += p
			if time > 0.1:
				data=data.split('\n') 
				#print data
				vol = data[0]
				voltage = float(vol)
				print voltage
				current = float(data[1])
				print current
				power = float(data[2])
				print power
				print power1

		else:
			power1=1000
			n1=ser.write('POW '+str(power1)+'\n')
			n2=ser.write('FETC:VOLT?\n')
			n3=ser.write('FETC:CURR?\n')
			n4=ser.write('FETC:POW?\n')
			data=''
			while ser.inWaiting() > 0:
				p=ser.read(1)
				data += p
			if time > 0.1:
				data=data.split('\n') 
				#print data
				vol = data[0]
				voltage = float(vol)
				print voltage
				current = float(data[1])
				print current
				power = float(data[2])
				print power
				print power1
		
	else:
		power1=1000-15*(time-80)
		if power1  < 1:
			power1 = 0

		n1=ser.write('POW '+str(power1)+'\n')
		n2=ser.write('FETC:VOLT?\n')
		n3=ser.write('FETC:CURR?\n')
		n4=ser.write('FETC:POW?\n')
		data=''
		while ser.inWaiting() > 0:
			p=ser.read(1)
			data += p
		if time > 0.1:
			data=data.split('\n') 
			#print data
			vol = data[0]
			voltage = float(vol)
			print voltage
			current = float(data[1])
			print current
			power = float(data[2])
			print power
			print power1
	
	global m
	m=m+1
	print 'm=' + str(m)

	#if m>1119:
	#	m=1119
	#	for a in range (1,1200,1):
			#x[a-1]=x[a]
	#		vp[a-1]=vp[a]
	#		cp[a-1]=cp[a]
	#		pp[a-1]=pp[a]
	#		p1p[a-1]=p1p[a]
	for a in range (1,1200,1):
		#x[a-1]=x[a]
		vp[a-1]=vp[a]
		cp[a-1]=cp[a]
		pp[a-1]=pp[a]
		p1p[a-1]=p1p[a]

	vp[1200-1]=voltage
	#print 'vol' + str(voltage)
	cp[1200-1]=current
	pp[1200-1]=power
	p1p[1200-1]=power1

	
	
	line1.set_data(x,vp)
	line2.set_data(x,cp)
	line3.set_data(x,pp)
	line4.set_data(x,p1p)
	
	ax1.grid(True)
	ax2.grid(True)
	ax3.grid(True)

	
	#x = np.linspace(0, 2, 100)   
	#y = np.sin(2 * np.pi * (x - 0.01 * i))  
	#line1.set_data(x, y)	  

	#x1 = np.linspace(0, 2, 100)   
	#y1 = np.cos(2 * np.pi * (x1 - 0.01 * i))* np.sin(2 * np.pi * (x - 0.01 * i))  
	#line2.set_data(x1, y1) 

	#x2 = np.linspace(0, 2, 100)   
	#y2 = np.cos(2 * np.pi * (x2 - 0.01 * i))* np.sin(2 * np.pi * (x - 0.01 * i))  
	#line3.set_data(x2, y2)   

	#line4.set_data(x1,y1)
	return line1,line2,line3,line4

anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=1200, interval=100)  
plt.show()
