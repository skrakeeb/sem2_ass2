'''
coded by: rakeeb 
coded for: solving boundary value problems using library function solve_bvp
** Here I followed the documentation of scipy
'''
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_bvp


def fun(x,y):
	return(np.vstack((y[1], y[1]*np.cos(x) - y[0]*np.log(y[0]))))

def bc(ya,yb):
	return(ya[0]-1 , yb[0]-np.e)
	

x= np.linspace(0,np.pi/2,10)

y_a= np.zeros((2,x.size))
y_b= np.zeros((2,x.size))
y_b[0]= 1.5

soln1= solve_bvp(fun,bc,x,y_a)
soln2= solve_bvp(fun,bc,x,y_b)	
x_plot= np.linspace(0,np.pi/2,100)
y_plot= soln1.sol(x_plot)[0]


plt.plot(x_plot,y_plot)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the 2nd solution')
plt.grid()
plt.show()