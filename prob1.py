'''
coded by: rakeeb 
coded for: implementation of implicit integration method
'''

import numpy as np 
import matplotlib.pyplot as plt 
import scipy.optimize as spo


#1st problem:
#exact solution:
x_exact= np.arange(0,1.01,0.01)
y_exact= np.exp(1-(9*x_exact))
plt.plot(x_exact,y_exact,'r',label= 'exact solution')

#by implicit method:
h= 0.05
x= np.arange(0,1.05,0.05)
y= np.zeros(21)
y[0]= np.e 
for i in range(20):
	y[i+1]= y[i]/(1+9*h)

plt.plot(x,y,'b',label= 'by implicit method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


#2nd problem:
h=0.05
x= np.arange(0,1.05,0.05)
y= np.zeros(21)
y[0]= 1/3.0

for i in range(20):
	m= x[i+1]
	n= y[i]
	def f(l):
		return(20*h*(l-m)**2+l-n-(2*h*m))	
	y[i+1]= spo.newton(f,1)   # solving the algebric eqn by Newton-Rapson method

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()		
	