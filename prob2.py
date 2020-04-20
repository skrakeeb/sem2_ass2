'''
coded by: rakeeb 
coded for: implimentation of Euler method
'''


import numpy as np 
import matplotlib.pyplot as plt 

t= np.arange(1,2.1,0.1)
y= np.zeros(11)
h= 0.1

def f(y1,t1):
	return((y1/t1)-(y1/t1)**2)
y[0]=1   # given initial condition
for i in range(10):
	y[i+1]= y[i]+h*f(y[i],t[i])

plt.plot(t,y,'b',label= 'by Euler method')

y_exact= t/(1+ np.log(t))
abs_err= abs(y_exact- y)  # absolute error array
mean_abs_err= np.mean(abs_err)  
rel_err= abs_err/y_exact   # relative error array
mean_rel_err= np.mean(rel_err)
print('mean absolute error:',mean_abs_err,'\nmean relative error: ',mean_rel_err)

plt.plot(t,y_exact,'r',label= 'exact solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()	