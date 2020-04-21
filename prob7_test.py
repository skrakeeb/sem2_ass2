'''
coded by: rakeeb 
coded for: solving differential eqn using library functions
** Unfortunately solve_ivp is not working in my computer. So I have used odeint function. 
'''
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint


def f1(y,t):
	return(t*np.exp(3*t) - 2*t)

t= np.arange(0,1.01,0.01)
y0= np.array([0])

y= odeint(f1,y0,t)
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plot of the 1st solution')
plt.grid()
plt.show()


def f2(y,t):
	return(1 - (t-y)**2)

t= np.arange(2,3.01,0.01)
y0= np.array([0])

y= odeint(f2,y0,t)
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plot of the 2nd solution')
plt.grid()
plt.show()


def f3(y,t):
	return(1 + y/t)

t= np.arange(1,2.01,0.01)
y0= np.array([2])

y= odeint(f3,y0,t)
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plot of the 3rd solution')
plt.grid()
plt.show()


def f4(y,t):
	return(np.cos(2*t) + np.sin(3*t))

t= np.arange(0,1.01,0.01)
y0= np.array([1])

y= odeint(f4,y0,t)
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plot of the 4th solution')
plt.grid()
plt.show()	
