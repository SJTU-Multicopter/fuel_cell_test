#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation   
import threading
from time import sleep

global xxx
xxx = 0

def loop1():
	global xxx
	xxx += 1
	print xxx
	sleep(1)

fig = plt.figure() 
ax1 = fig.add_subplot(2,1,1,xlim=(0, 2), ylim=(-4, 4)) #graph length, height, index, x range, y range
ax2 = fig.add_subplot(2,1,2,xlim=(0, 2), ylim=(-4, 4))
line, = ax1.plot([], [], lw=2) 
line1, = ax1.plot([], [], lw=2) 
line2, = ax2.plot([], [], lw=2)  
def init():  
	line.set_data([], [])  
	line2.set_data([], [])  
	return line,line2

# animation function.  this is called sequentially   
def animate(i):
	global xxx

	x = np.linspace(0, 2, 100)   
	y = np.sin(2 * np.pi * (x - 0.01 * i))  
	line.set_data(x, y)	  

	x1 = np.linspace(0, 2, 100)   
	y1 = np.cos(2 * np.pi * (x1 - 0.01 * i))* np.sin(2 * np.pi * (x - 0.01 * i))  
	line1.set_data(x1, y1) 

	x2 = np.linspace(0, 2, 100)   
	y2 = np.cos(2 * np.pi * (x2 - 0.01 * i))* np.sin(2 * np.pi * (x - 0.01 * i)) + xxx 
	line2.set_data(x2, y2)   
	return line,line1,line2

l1 = threading.Thread(target=loop1,args='')
l1.start()

anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=50, interval=10)  
plt.show()





