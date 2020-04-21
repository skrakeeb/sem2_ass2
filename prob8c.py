'''
coded by: rakeeb 
coded for: solving boundary value problems using library function solve_bvp
** Here I followed the documentation of scipy
'''
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_bvp

def fun(x,y):
	return(np.vstack((y[1], - (2*y[1]**3 + y[1]*y[0]**2)/(np.cos(x)) )))

def bc(ya,yb):
	return(ya[0]- 2**(-1.0/4), yb[0]- (12**(1.0/4)/2))

x= np.linspace(np.pi/4, np.pi/3, 5)

y_a= np.zeros((2,x.size))
y_b= np.zeros((2,x.size))
y_b[0]= 10

soln1= solve_bvp(fun,bc,x,y_a)
soln2= solve_bvp(fun,bc,x,y_b)	
x_plot= np.linspace(np.pi/4, np.pi/3,100)
y_plot= soln1.sol(x_plot)[0]


plt.plot(x_plot,y_plot)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the 3rd solution')
plt.grid()
plt.show()