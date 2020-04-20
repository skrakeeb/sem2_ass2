'''
coded by: rakeeb 
coded for: implimentation of 2nd order Runge-Kutta method
'''

import numpy as np 
import matplotlib.pyplot as plt 


x= np.arange(0,1.1,0.1)
h= 0.1
v= np.zeros(x.size)  # v=y'
y= np.zeros(x.size)
v[0]=0
y[0]=0
def f1(x1,y1,v1):   #for solving the eqn y'= v
	return(v1)

def f2(x1,y1,v1):   #for solving the eqn y''= f(x,y,y')
	return(2*v1-y1-x1+(x1*np.exp(x1)))

for i in range(10):
	k10= h*f1(x[i],y[i],v[i])
	k20= h*f2(x[i],y[i],v[i])

	k11= h*f1(x[i]+h/2,y[i]+k10/2,v[i]+k20/2)
	k21= h*f2(x[i]+h/2,y[i]+k10/2,v[i]+k20/2)

	y[i+1]= y[i]+k11
	v[i+1]= v[i]+k21
	
plt.plot(x,y,'r',label='y')
plt.plot(x,v,'b',label='dy/dx')
plt.xlabel('x')
plt.legend()
plt.grid()
plt.show()




