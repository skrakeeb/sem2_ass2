'''
coded by: rakeeb 
coded for: Implementation of Euler method for second order
'''
import numpy as np 
import matplotlib.pyplot as plt 

t= np.arange(1,2.001,0.001)
h= 0.001
v= np.zeros(1001)  # v=y'
y= np.zeros(1001)
v[0]=0
y[0]=1
def f1(t1,y1,v1):   #for solving the eqn y'= v
	return(v1)

def f2(t1,y1,v1):   #for solving the eqn y''= f(x,y,y')
	return((2/t1)*v1 - 2*y1/(t1**2) + t1*np.log(t1))

for i in range(1000):
	y[i+1]= y[i]+h*f1(t[i],y[i],v[i])
	v[i+1]= v[i]+h*f2(t[i],y[i],v[i])

def f_exact(t2):
	return(7*t2/4 + (np.log(t2)*t2**3)/2 - (3*t2**3)/4)

y_exact= f_exact(t)	

plt.plot(t,y,'r',label='by Euler method')
plt.plot(t,y_exact,'b',label='Exact solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.show()


