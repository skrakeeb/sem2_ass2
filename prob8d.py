'''
coded by: rakeeb 
coded for: solving boundary value problems using library function solve_bvp
** Here I followed the documentation of scipy
'''
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_bvp

def fun(x,y):
	return(np.vstack((y[1], 1/2 - (y[1]**2)/2 - y[0]*np.sin(x)/2 )))

def bc(ya,yb):
	return(ya[0]-2, yb[0]-2)

x= np.linspace(0,np.pi,5)

y_a= np.zeros((2,x.size))
y_b= np.zeros((2,x.size))
y_b[0]= 5

soln1= solve_bvp(fun,bc,x,y_a)
soln2= solve_bvp(fun,bc,x,y_b)	
x_plot= np.linspace(0,np.pi,100)
y_plot= soln1.sol(x_plot)[0]


plt.plot(x_plot,y_plot)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the 4th solution')
plt.grid()
plt.show()
